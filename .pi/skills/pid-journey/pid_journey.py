#!/usr/bin/env python3
"""
pid_journey.py

Local journey planner for Prague (PID) using GTFS (no API key required).

Usage examples:
  ./pid_journey.py fetch --refresh
  ./pid_journey.py plan --from "Anděl" --to "Národní třída" --date 2026-04-22 --time 18:00 --mode departure --max-transfers 2

Notes:
- First run will download and extract GTFS into ./data/
- Prototype: focuses on correct timetable logic (services, trips, stop_times) and RAPTOR-style search with transfer limits.
"""

from __future__ import annotations
import os
import sys
import csv
import argparse
import urllib.request
import zipfile
import tempfile
import shutil
import pickle
import time
from datetime import datetime, date
from zoneinfo import ZoneInfo
from collections import defaultdict, deque
from typing import Dict, List, Tuple, Optional, Any

# Config
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, 'data')
GTFS_ZIP_URL = 'https://data.pid.cz/PID_GTFS.zip'
GTFS_ZIP_PATH = os.path.join(DATA_DIR, 'PID_GTFS.zip')
GTFS_EXTRACT_DIR = os.path.join(DATA_DIR, 'gtfs')
CACHE_PATH = os.path.join(DATA_DIR, 'cache.pkl')

PRAGUE_TZ = ZoneInfo('Europe/Prague')

# Utility
def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def download_gtfs(force: bool = False) -> None:
    ensure_data_dir()
    if os.path.exists(GTFS_EXTRACT_DIR) and not force:
        print(f"GTFS already extracted in {GTFS_EXTRACT_DIR}. Use --refresh to re-download.")
        return
    if force and os.path.exists(GTFS_EXTRACT_DIR):
        shutil.rmtree(GTFS_EXTRACT_DIR)
    print('Downloading GTFS feed (PID)...')
    tmp = GTFS_ZIP_PATH + '.part'
    try:
        urllib.request.urlretrieve(GTFS_ZIP_URL, tmp)
        os.replace(tmp, GTFS_ZIP_PATH)
    except Exception as e:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise
    print('Extracting...')
    with zipfile.ZipFile(GTFS_ZIP_PATH, 'r') as z:
        z.extractall(GTFS_EXTRACT_DIR)
    print('GTFS ready in', GTFS_EXTRACT_DIR)


# GTFS parsing helpers

def parse_time_to_seconds(ts: str) -> Optional[int]:
    # GTFS allows HH:MM:SS where HH may be >= 24
    if ts is None:
        return None
    ts = ts.strip()
    if ts == '':
        return None
    try:
        parts = ts.split(':')
        if len(parts) != 3:
            return None
        h, m, s = int(parts[0]), int(parts[1]), int(parts[2])
        return h * 3600 + m * 60 + s
    except Exception:
        return None


def read_csv(path: str):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


# Service calendar

def services_active_on(gtfs_dir: str, when: date) -> set:
    # calendar.txt and calendar_dates.txt
    service_ids = set()
    cal_path = os.path.join(gtfs_dir, 'calendar.txt')
    cal_dates_path = os.path.join(gtfs_dir, 'calendar_dates.txt')

    weekday_name = when.strftime('%A').lower()  # monday, tuesday...
    weekday_field = weekday_name[:3]  # mon, tue... but GTFS uses monday,tuesday
    # we'll check full names
    if os.path.exists(cal_path):
        for row in read_csv(cal_path):
            sid = row.get('service_id')
            try:
                start = datetime.strptime(row.get('start_date'), '%Y%m%d').date()
                end = datetime.strptime(row.get('end_date'), '%Y%m%d').date()
            except Exception:
                continue
            if not (start <= when <= end):
                continue
            dow = when.strftime('%A').lower()  # e.g., monday
            if row.get(dow, '0') == '1':
                service_ids.add(sid)
    # apply exceptions
    if os.path.exists(cal_dates_path):
        for row in read_csv(cal_dates_path):
            sid = row.get('service_id')
            try:
                d = datetime.strptime(row.get('date'), '%Y%m%d').date()
            except Exception:
                continue
            et = row.get('exception_type')
            if d == when:
                if et == '1':
                    service_ids.add(sid)
                elif et == '2':
                    if sid in service_ids:
                        service_ids.remove(sid)
    return service_ids


# Build timetable structures

class Stop:
    def __init__(self, stop_id: str, name: str, lat: Optional[float], lon: Optional[float]):
        self.id = stop_id
        self.name = name
        self.lat = lat
        self.lon = lon


class Trip:
    def __init__(self, trip_id: str, route_id: str, service_id: str, direction_id: Optional[str], trip_headsign: Optional[str]):
        self.id = trip_id
        self.route_id = route_id
        self.service_id = service_id
        self.direction_id = direction_id
        self.trip_headsign = trip_headsign
        # stop_times: list of dicts {stop_idx, arrival, departure, stop_id, stop_sequence}
        self.stop_times: List[Dict[str, Any]] = []


def build_timetable(gtfs_dir: str, when: date) -> Dict[str, Any]:
    # Parse stops, trips, stop_times, routes, transfers
    print('Parsing GTFS files...')
    stops = {}
    stops_list = []
    stops_path = os.path.join(gtfs_dir, 'stops.txt')
    if os.path.exists(stops_path):
        for r in read_csv(stops_path):
            sid = r.get('stop_id')
            name = r.get('stop_name') or ''
            lat = None
            lon = None
            try:
                lat = float(r.get('stop_lat'))
                lon = float(r.get('stop_lon'))
            except Exception:
                pass
            stops[sid] = Stop(sid, name, lat, lon)
            stops_list.append(sid)
    else:
        print('stops.txt not found in GTFS')

    # routes
    routes = {}
    routes_path = os.path.join(gtfs_dir, 'routes.txt')
    if os.path.exists(routes_path):
        for r in read_csv(routes_path):
            routes[r.get('route_id')] = r

    # trips
    trips_file = os.path.join(gtfs_dir, 'trips.txt')
    trips_rows = []
    if os.path.exists(trips_file):
        trips_rows = read_csv(trips_file)
    trips_map: Dict[str, Trip] = {}
    # filter by active services
    active_services = services_active_on(gtfs_dir, when)
    print(f'Active services on {when}: {len(active_services)}')
    for r in trips_rows:
        sid = r.get('service_id')
        if sid not in active_services:
            continue
        tid = r.get('trip_id')
        trip = Trip(trip_id=tid, route_id=r.get('route_id'), service_id=sid, direction_id=r.get('direction_id'), trip_headsign=r.get('trip_headsign'))
        trips_map[tid] = trip

    # stop_times
    st_path = os.path.join(gtfs_dir, 'stop_times.txt')
    if os.path.exists(st_path):
        for r in read_csv(st_path):
            tid = r.get('trip_id')
            if tid not in trips_map:
                continue
            arr_s = parse_time_to_seconds(r.get('arrival_time'))
            dep_s = parse_time_to_seconds(r.get('departure_time'))
            stop_id = r.get('stop_id')
            seq = int(r.get('stop_sequence') or 0)
            trips_map[tid].stop_times.append({'stop_id': stop_id, 'stop_sequence': seq, 'arrival': arr_s, 'departure': dep_s})
    # sort stop_times by sequence
    for t in list(trips_map.values()):
        t.stop_times.sort(key=lambda x: x['stop_sequence'])

    # optionally, remove trips with less than 2 stops
    trips_map = {tid: t for tid, t in trips_map.items() if len(t.stop_times) >= 2}
    print(f'Trips active: {len(trips_map)}')

    # transfers
    transfers = defaultdict(list)  # from_stop -> list of (to_stop, min_transfer_time_seconds)
    transfers_path = os.path.join(gtfs_dir, 'transfers.txt')
    if os.path.exists(transfers_path):
        for r in read_csv(transfers_path):
            from_s = r.get('from_stop_id')
            to_s = r.get('to_stop_id')
            mt = r.get('min_transfer_time')
            try:
                mtv = int(mt) if mt else 0
            except Exception:
                mtv = 0
            transfers[from_s].append((to_s, mtv))
    # ensure self-transfer 0
    for sid in stops.keys():
        transfers[sid].append((sid, 0))

    # Build index: stop_id -> list of (trip_id, index_in_trip)
    stop_to_trip_events = defaultdict(list)
    for tid, trip in trips_map.items():
        for idx, st in enumerate(trip.stop_times):
            stop_to_trip_events[st['stop_id']].append((tid, idx))

    # route info mapping
    routes_info = {}
    for rid, r in routes.items():
        routes_info[rid] = r

    timetable = {
        'stops': stops,
        'trips': trips_map,
        'stop_to_trip_events': stop_to_trip_events,
        'transfers': transfers,
        'routes': routes_info,
        'built_at': time.time()
    }
    return timetable


# RAPTOR implementation

INF = 10 ** 12


def format_seconds_hm(s: Optional[int]) -> str:
    if s is None:
        return '?'
    h = s // 3600
    m = (s % 3600) // 60
    return f"{h:02d}:{m:02d}"


def raptor_search(timetable: Dict[str, Any], src_stop_id: str, dst_stop_id: str, departure_time: int, max_transfers: int = 2, reverse: bool = False) -> Optional[Dict[str, Any]]:
    # reverse=False for departure search (earliest arrival given departure_time)
    # reverse=True for arrival search (we run RAPTOR on reversed trips and swap src/dst)
    stops = timetable['stops']
    trips = timetable['trips']
    stop_to_trip_events = timetable['stop_to_trip_events']
    transfers = timetable['transfers']

    if src_stop_id not in stops or dst_stop_id not in stops:
        print('Unknown stop ids')
        return None

    # For reverse mode we need reversed trips built on the fly
    if reverse:
        # Build a reversed view of trips: for each trip create stop_times_rev list where index j corresponds to original n-1-j
        trips_rev = {}
        stop_to_trip_events_rev = defaultdict(list)
        for tid, trip in trips.items():
            orig = trip.stop_times
            n = len(orig)
            # build rev stop_times with arrival_rev = original.departure[orig_idx], departure_rev = original.arrival[orig_idx]
            rev_st = []
            for j in range(n-1, -1, -1):
                orig_entry = orig[j]
                rev_st.append({'stop_id': orig_entry['stop_id'], 'arrival': orig_entry['departure'], 'departure': orig_entry['arrival'], 'stop_sequence': orig_entry['stop_sequence']})
            t2 = Trip(trip.id, trip.route_id, trip.service_id, trip.direction_id, trip.trip_headsign)
            t2.stop_times = rev_st
            trips_rev[tid] = t2
            for idx, st in enumerate(t2.stop_times):
                stop_to_trip_events_rev[st['stop_id']].append((tid, idx))
        trips_use = trips_rev
        stop_to_trip_events_use = stop_to_trip_events_rev
    else:
        trips_use = trips
        stop_to_trip_events_use = stop_to_trip_events

    # Map stop ids to integers for arrays
    stop_ids = list(stops.keys())
    stop_index = {sid: i for i, sid in enumerate(stop_ids)}
    n_stops = len(stop_ids)

    if src_stop_id not in stop_index or dst_stop_id not in stop_index:
        print('Stops not in index')
        return None

    src_idx = stop_index[src_stop_id]
    dst_idx = stop_index[dst_stop_id]

    # We'll store earliest_arrival_per_round[r][stop_idx] = time
    rounds = max_transfers + 1
    earliest = [[INF] * n_stops for _ in range(rounds + 1)]
    # predecessor info per round and stop
    pred = [dict() for _ in range(rounds + 1)]

    earliest[0][src_idx] = departure_time
    pred[0][src_idx] = {'type': 'start'}
    marked_stops = set([src_stop_id])

    # For optimization: precompute trip stop_times arrays for fast access
    # trips_use is mapping trip_id -> Trip

    for r in range(rounds):
        # candidate boardings per trip: trip_id -> (boarding_stop_id, boarding_index)
        trip_board = {}
        trip_board_time = {}

        # 1) For each marked stop, find trip events where you can board
        for s in marked_stops:
            s_idx = stop_index[s]
            t_available = earliest[r][s_idx]
            if t_available >= INF:
                continue
            events = stop_to_trip_events_use.get(s, [])
            for tid, idx_in_trip in events:
                trip = trips_use.get(tid)
                if not trip:
                    continue
                # departure time at that stop
                st_entry = trip.stop_times[idx_in_trip]
                dep_time = st_entry.get('departure')
                if dep_time is None:
                    # if departure missing, try arrival
                    dep_time = st_entry.get('arrival')
                if dep_time is None:
                    continue
                # can we catch it?
                if dep_time < t_available:
                    continue
                # register candidate boarding - prefer earliest index in trip (lowest index) for which condition holds
                prev = trip_board.get(tid)
                if prev is None or idx_in_trip < prev:
                    trip_board[tid] = idx_in_trip
                    trip_board_time[tid] = dep_time

        # 2) Scan each trip that has a boarding candidate
        newly_marked = set()
        for tid, board_idx in trip_board.items():
            trip = trips_use[tid]
            board_stop_id = trip.stop_times[board_idx]['stop_id']
            board_time = trip.stop_times[board_idx].get('departure') or trip.stop_times[board_idx].get('arrival')
            # propagate to subsequent stops
            for j in range(board_idx + 1, len(trip.stop_times)):
                st = trip.stop_times[j]
                stop_j = st['stop_id']
                arr_time = st.get('arrival')
                if arr_time is None:
                    continue
                si = stop_index.get(stop_j)
                if si is None:
                    continue
                if arr_time < earliest[r + 1][si]:
                    earliest[r + 1][si] = arr_time
                    # predecessor: this stop_j at round r+1 was reached by boarding tid at board_stop_id
                    pred[r + 1][si] = {
                        'type': 'transit',
                        'trip_id': tid,
                        'board_stop_id': board_stop_id,
                        'board_time': board_time,
                        'alight_stop_id': stop_j,
                        'alight_time': arr_time,
                        'boarded_round': r
                    }
                    newly_marked.add(stop_j)
        # 3) Apply transfers (footpaths) from newly_marked stops within same round r+1
        # Also include direct transfer from a stop to itself (0) already present
        changed = True
        # We'll do simple propagation: for every stop updated in this round, try to relax its footpaths
        # iterate until no change
        queue = deque(newly_marked)
        while queue:
            s = queue.popleft()
            si = stop_index[s]
            s_time = earliest[r + 1][si]
            for to_stop, ttime in transfers.get(s, []):
                ti = stop_index.get(to_stop)
                if ti is None:
                    continue
                cand = s_time + int(ttime)
                if cand < earliest[r + 1][ti]:
                    earliest[r + 1][ti] = cand
                    pred[r + 1][ti] = {
                        'type': 'transfer',
                        'from_stop_id': s,
                        'to_stop_id': to_stop,
                        'transfer_time': int(ttime)
                    }
                    queue.append(to_stop)
                    newly_marked.add(to_stop)
        # 4) Prepare marked_stops for next round: those improved in r+1 compared to any earlier round
        next_marked = set()
        for sid in newly_marked:
            si = stop_index[sid]
            # check if earliest[r+1][si] improved (we know it did) and is useful
            next_marked.add(sid)
        marked_stops = next_marked
        # early exit if destination reached and no further improvement expected
        dst_time = earliest[r + 1][dst_idx]
        if dst_time < INF:
            # we could break early but might find a better solution with more transfers; continue rounds
            pass
        if not marked_stops:
            break
    # choose best round where dst has minimal arrival
    best_time = INF
    best_round = None
    for r in range(rounds + 1):
        if earliest[r][dst_idx] < best_time:
            best_time = earliest[r][dst_idx]
            best_round = r
    if best_time >= INF:
        return None

    # reconstruct path from dst at best_round
    itinerary = []
    cur_stop = dst_stop_id
    cur_round = best_round
    cur_idx = dst_idx
    while True:
        info = pred[cur_round].get(cur_idx)
        if info is None:
            break
        if info.get('type') == 'start':
            break
        if info.get('type') == 'transfer':
            # transfer from from_stop_id -> to_stop_id (to_stop should equal cur_stop)
            from_stop = info['from_stop_id']
            itinerary.append({'type': 'walk', 'from': from_stop, 'to': cur_stop, 'time': info['transfer_time']})
            cur_stop = from_stop
            cur_idx = stop_index[cur_stop]
            # remains in same round
            continue
        if info.get('type') == 'transit':
            trip_id = info['trip_id']
            board_stop = info['board_stop_id']
            alight_stop = info['alight_stop_id']
            board_time = info['board_time']
            alight_time = info['alight_time']
            # append trip leg
            itinerary.append({'type': 'ride', 'trip_id': trip_id, 'from': board_stop, 'to': alight_stop, 'dep': board_time, 'arr': alight_time})
            # set cur_stop to board_stop and move to boarded_round
            cur_stop = board_stop
            cur_idx = stop_index[cur_stop]
            cur_round = info['boarded_round']
            continue
    itinerary.reverse()
    return {'from': src_stop_id, 'to': dst_stop_id, 'departure_time': departure_time, 'arrival_time': best_time, 'rounds_used': best_round, 'itinerary': itinerary}


# Helper: fuzzy search stop name

def find_stops_by_name(stops: Dict[str, Stop], q: str) -> List[Tuple[str, Stop]]:
    ql = q.lower()
    matches = []
    for sid, st in stops.items():
        if ql in (st.name or '').lower():
            matches.append((sid, st))
    # sort by exactness (starts-with first)
    matches.sort(key=lambda x: (0 if x[1].name.lower().startswith(ql) else 1, x[1].name))
    return matches


# High-level CLI

def load_timetable(date_obj: date, refresh=False):
    ensure_data_dir()
    if refresh or not os.path.exists(GTFS_EXTRACT_DIR):
        download_gtfs(force=refresh)
    # try load cache
    if os.path.exists(CACHE_PATH) and not refresh:
        try:
            with open(CACHE_PATH, 'rb') as f:
                cache = pickle.load(f)
            # check if cached for same date
            key_date = cache.get('date')
            if key_date == date_obj.isoformat():
                print('Loaded timetable from cache')
                return cache['timetable']
        except Exception:
            pass
    # build timetable
    t = build_timetable(GTFS_EXTRACT_DIR, date_obj)
    try:
        with open(CACHE_PATH, 'wb') as f:
            pickle.dump({'date': date_obj.isoformat(), 'timetable': t}, f)
    except Exception:
        pass
    return t


def select_stop_interactive(stops: Dict[str, Stop], query: str) -> Optional[str]:
    matches = find_stops_by_name(stops, query)
    if not matches:
        print('No stops matching', query)
        return None
    if len(matches) == 1:
        print(f"Selected: {matches[0][1].name} ({matches[0][0]})")
        return matches[0][0]
    # interactive selection
    print('Multiple matches:')
    for i, (sid, st) in enumerate(matches[:20]):
        print(f"[{i}] {st.name} ({sid})")
    try:
        idx = int(input('Choose index (default 0): ') or '0')
    except Exception:
        idx = 0
    if idx < 0 or idx >= len(matches):
        idx = 0
    return matches[idx][0]


def cmd_fetch(args):
    download_gtfs(force=args.refresh)


def cmd_plan(args):
    # parse date and time
    if args.date:
        d = datetime.strptime(args.date, '%Y-%m-%d').date()
    else:
        d = datetime.now(PRAGUE_TZ).date()
    try:
        tparts = args.time.split(':')
        hh = int(tparts[0]); mm = int(tparts[1])
        departure_seconds = hh * 3600 + mm * 60
    except Exception:
        print('Time format should be HH:MM')
        return

    timetable = load_timetable(d, refresh=args.refresh)
    stops = timetable['stops']

    # resolve from/to
    if args.from_id:
        from_id = args.from_id
    else:
        from_id = None
    if args.to_id:
        to_id = args.to_id
    else:
        to_id = None
    if not from_id:
        from_id = select_stop_interactive(stops, args.from_name)
        if not from_id:
            return
    if not to_id:
        to_id = select_stop_interactive(stops, args.to_name)
        if not to_id:
            return

    mode = args.mode or 'departure'
    max_transfers = int(args.max_transfers or 2)
    if args.direct:
        max_transfers = 0

    reverse = False
    if mode == 'arrival':
        reverse = True
        # For arrival mode we will run reversed RAPTOR starting from destination; but our raptor_search expects src/dst in its logic
        # We'll call raptor_search with reverse=True and swap src/dst
        src = to_id
        dst = from_id
    else:
        src = from_id
        dst = to_id

    print(f"Searching {mode} from {stops[src].name} ({src}) to {stops[dst].name} ({dst}) on {d} at {args.time} with max_transfers={max_transfers}")

    result = raptor_search(timetable, src, dst, departure_seconds, max_transfers=max_transfers, reverse=reverse)
    if not result:
        print('No connection found')
        return

    # if arrival mode, result departure_time/arrival_time correspond to reversed timeline; adjust printing by swapping
    if mode == 'arrival':
        # result contains from=to_id, to=from_id, departure_time = requested arrival_time
        # convert to user-facing legs by flipping each 'ride' leg: swap from/to
        # But our reconstruction produced itinerary in reversed direction. We'll invert each ride leg.
        it = result['itinerary']
        # revert itinerary legs
        new_it = []
        for leg in it:
            if leg['type'] == 'ride':
                # leg currently is from board_stop->alight_stop in reversed trip; invert
                new_it.append({'type': 'ride', 'trip_id': leg['trip_id'], 'from': leg['to'], 'to': leg['from'], 'dep': leg['arr'], 'arr': leg['dep']})
            else:
                # walk legs reversed
                new_it.append({'type': 'walk', 'from': leg['to'], 'to': leg['from'], 'time': leg.get('time', 0)})
        result['itinerary'] = new_it
        # swap reported times
        # original result['departure_time'] is arrival_time requested; result['arrival_time'] is derived earliest departure (in reversed chronology), so swap
        reported_departure = result['arrival_time']
        reported_arrival = result['departure_time']
    else:
        reported_departure = result['departure_time']
        reported_arrival = result['arrival_time']

    print('\nResult:')
    print(f"Departure: {format_seconds_hm(reported_departure)} — Arrival: {format_seconds_hm(reported_arrival)} (transfers used: {result['rounds_used']})")
    print('\nItinerary:')
    for leg in result['itinerary']:
        if leg['type'] == 'ride':
            trip_id = leg['trip_id']
            route = timetable['trips'][trip_id].route_id if trip_id in timetable['trips'] else '?'
            route_name = timetable['routes'].get(route, {}).get('route_short_name') if timetable.get('routes') else route
            print(f"  RIDE {route_name or route} | {stops[leg['from']].name} ({leg['from']}) -> {stops[leg['to']].name} ({leg['to']}) | {format_seconds_hm(leg['dep'])} -> {format_seconds_hm(leg['arr'])}")
        else:
            print(f"  WALK {stops[leg['from']].name} ({leg['from']}) -> {stops[leg['to']].name} ({leg['to']}) ~ {leg.get('time',0)}s")


def build_parser():
    p = argparse.ArgumentParser(description='PID Journey planner (GTFS local, no API key)')
    sub = p.add_subparsers(dest='cmd')

    f = sub.add_parser('fetch', help='Download/refresh GTFS feed')
    f.add_argument('--refresh', action='store_true', help='Force re-download and re-extract')
    f.set_defaults(func=cmd_fetch)

    plan = sub.add_parser('plan', help='Plan a journey')
    plan.add_argument('--from-name', dest='from_name', help='Stop name to start from')
    plan.add_argument('--to-name', dest='to_name', help='Stop name to go to')
    plan.add_argument('--from-id', dest='from_id', help='GTFS stop_id for start')
    plan.add_argument('--to-id', dest='to_id', help='GTFS stop_id for destination')
    plan.add_argument('--date', help='Date YYYY-MM-DD (default: today)')
    plan.add_argument('--time', required=True, help='Time HH:MM (required)')
    plan.add_argument('--mode', choices=['departure', 'arrival'], default='departure', help='Search mode')
    plan.add_argument('--max-transfers', default=2, help='Maximum transfers allowed (default 2)')
    plan.add_argument('--direct', action='store_true', help='Direct-only (equivalent to --max-transfers 0)')
    plan.add_argument('--refresh', action='store_true', help='Refresh GTFS data before planning')
    plan.set_defaults(func=cmd_plan)

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.cmd:
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == '__main__':
    raise SystemExit(main())
