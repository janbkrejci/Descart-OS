#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""
Get gold bar prices from the MIG GraphQL endpoint used by Investicnicentrum / CSAS.

This tool script is executable and intended to be run directly (ex. ./tools/csas_gold/get_gold_price.py).
It uses only Python standard library modules.
"""
import argparse
import json
import sys
import urllib.request
import datetime
from zoneinfo import ZoneInfo

NOTATION_MAP = {
    "10": "F74258039",
    "31.1": "F124217074",
    "50": "F74258117",
    "100": "F74258118",
}

GRAPHQL_URL = "https://mig.erstegroup.com/gql/cz-mdp/"

QUERY = """
query getInstruments($notationIds:[NotationId!]!){
  instruments(notationIds:$notationIds){
    id
    name{full short}
    notation{
      id
      symbol
      unit{code name}
      tradingInfo{
        p1D{
          bid{price{value currency}}
          ask{price{value currency}}
          last{price{value currency} dateTime}
        }
      }
    }
  }
}
"""


def format_currency(value):
    if value is None:
        return "-"
    try:
        v = float(value)
    except Exception:
        return str(value)
    # English-style formatting: 306,406.00
    return f"{v:,.2f}"


def query_mig(notation_ids):
    payload = {"query": QUERY, "variables": {"notationIds": notation_ids}}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(GRAPHQL_URL, data=data, headers={"Content-Type": "application/json; charset=UTF-8"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def format_datetime_iso_to_prague(iso):
    if not iso:
        return None
    try:
        dt = datetime.datetime.fromisoformat(iso.replace('Z', '+00:00'))
        dt = dt.astimezone(ZoneInfo('Europe/Prague'))
        return dt.strftime('%Y-%m-%d %H:%M:%S %Z')
    except Exception:
        return iso


def main():
    parser = argparse.ArgumentParser(description="Get buy/sell prices for gold bars (CSAS / Investicnicentrum) via MIG GraphQL.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--weight", "-w", default="100", help="Gold bar weight in grams (10, 31.1, 50, 100). Default: 100.")
    group.add_argument("--notation", "-n", help="Direct notationId (e.g. F74258118).")
    parser.add_argument("--json", action="store_true", help="Print raw JSON response from API.")
    args = parser.parse_args()

    if args.notation:
        notation_ids = [args.notation]
    else:
        w = args.weight
        if w not in NOTATION_MAP:
            print("Unknown weight. Supported: " + ", ".join(NOTATION_MAP.keys()), file=sys.stderr)
            sys.exit(2)
        notation_ids = [NOTATION_MAP[w]]

    try:
        resp = query_mig(notation_ids)
    except Exception as e:
        print("Error calling API:", e, file=sys.stderr)
        sys.exit(3)

    if args.json:
        print(json.dumps(resp, ensure_ascii=False, indent=2))
        return

    if "errors" in resp:
        print("API returned errors:", file=sys.stderr)
        print(json.dumps(resp["errors"], ensure_ascii=False, indent=2), file=sys.stderr)
        sys.exit(4)

    instruments = resp.get("data", {}).get("instruments", [])
    if not instruments:
        print("No instruments found.", file=sys.stderr)
        sys.exit(5)

    for inst in instruments:
        name_full = inst.get("name", {}).get("full")
        notation = inst.get("notation", {})
        notation_id = notation.get("id")
        symbol = notation.get("symbol")
        unit = notation.get("unit", {}).get("code", "CZK")
        tinfo = notation.get("tradingInfo", {}).get("p1D", {})
        bid = tinfo.get("bid", {}).get("price", {})
        ask = tinfo.get("ask", {}).get("price", {})
        last = tinfo.get("last", {}).get("price", {})
        last_dt = tinfo.get("last", {}).get("dateTime")

        print(f"Product: {name_full} (notationId: {notation_id}, symbol: {symbol})")
        bid_val = bid.get('value') if isinstance(bid, dict) else None
        ask_val = ask.get('value') if isinstance(ask, dict) else None
        last_val = last.get('value') if isinstance(last, dict) else None

        print(f"Buy (bid): {format_currency(bid_val)} {bid.get('currency') if bid.get('currency') else unit}")
        print(f"Sell (ask): {format_currency(ask_val)} {ask.get('currency') if ask.get('currency') else unit}")
        if last_val is not None:
            print(f"Last price: {format_currency(last_val)} {last.get('currency') if last.get('currency') else unit}")
        if last_dt:
            print("Last update:", format_datetime_iso_to_prague(last_dt))
        print()


if __name__ == '__main__':
    main()
