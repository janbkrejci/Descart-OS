---
name: write_md
description: Nástroj pro vytváření a úpravu markdown souborů.
---
# Vytváření a úprava markdown souborů

Tato dovednost mi umožňuje na žádost uživatele samostatně vytvářet a upravovat markdown soubory na disku.

## Omezení, která musím striktně dodržet

1. Nikdy nesmím upravovat soubor .pi/SYSTEM.md

## Postup, který musím striktně dodržet:

1. Ujistím se, že vím jméno a cestu k souboru, a co má soubor obsahovat.
2. Využiji povolený interní nástroj `write` pro přepsání celého souboru, nebo `edit` pro úpravu obsahu existujícího souboru a zajistím, aby soubor měl požadovaný obsah.
3. Zajistím, aby v markdown souboru vždy byl na začátku povinný YAML frontmatter (minimálně s klíči `name` a `description`).
4. Zkontroluji pomocí interního nástroje `read`, že obsah souboru je přesně takový, jaký byl požadován.
5. Po úspěšném provedení uživatele informuji, že byl soubor vytvořen nebo upraven dle požadavku.