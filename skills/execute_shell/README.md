---
name: execute_shell
description: Dovednost používat nástroj shell pro spouštění příkazů v tmuxu a zpracování jejich výstupu.
---

# Spouštění a zpracování shell příkazů v tmuxu

Tato dovednost mi předepisuje, jak samostatně využívat nástroj `shell` (který vespod používá systémový `bash` a `tmux`) pro spouštění příkazů zadaných uživatelem a získání jejich výstupu k dalšímu zpracování.

## Postup, který musím striktně dodržet:
1. Ujistím se, že vím přesně, jaký shell příkaz má být spuštěn.
2. Samotné spuštění příkazu (včetně obalení syntaxí pro `tmux` a získání výstupu) plně deleguji na nástroj `shell` podle jeho pravidel.
3. Přečtu a zanalyzuji celý získaný výstup z nástroje `shell`.
4. Seznámím uživatele s výsledkem operace přehledně, strukturovaně a stručně, s případným návrhem na další kroky.
