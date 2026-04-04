---
name: shell
description: Nástroj pro provedení zadaného příkazu v tmuxu a vrácení jeho výstupu.
---

# Shell (tmux)

Tento nástroj mi umožňuje spustit bash příkaz v multiplexeru `tmux` a získat zpět jeho výstup. K faktickému vykonání příkazů využívám svůj systémový nástroj `bash`.

## Použití a pravidla
1. K provedení akce použiji systémový nástroj `bash`.
2. Příkaz zadaný uživatelem provedu v rámci `tmux` sezení (např. pomocí `tmux new-session`, `tmux send-keys`, atd.).
3. Následně zachytím výsledek příkazu (např. pomocí přesměrování do souboru nebo přes `tmux capture-pane -p`) a zajistím, že nezůstanou viset prázdná či zbytečná okna.
4. Pokud příkaz běží dlouho, tmux mi umožní oddělit proces na pozadí a později zkontrolovat jeho výstup.
