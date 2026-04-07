---
name: csas_gold_skill
description: Skill for fetching current buy/sell prices for gold bars (CSAS / Investicnicentrum) via the MIG GraphQL API.
---

# CSAS Gold Prices Skill

This skill allows me to fetch the current buy (bid) and sell (ask) prices for gold bars from the Investicnicentrum (Česká spořitelna) website. The data is obtained from the public MIG GraphQL endpoint.

## Procedure I must follow

1. When the user asks for current gold prices, I will execute the Python script located at `tools/csas_gold/get_gold_price.py` using the `bash` tool.
2. The script supports different weights of gold bars. I can specify the weight using the `--weight` nebo `-w` parameter (supported weights: `10`, `31.1`, `50`, `100`). If no weight is specified, the default is `100` grams.
   Example:
   ```bash
   python3 tools/csas_gold/get_gold_price.py -w 100
   ```
3. To obtain raw JSON data for custom calculations or parsing, I will use the `--json` flag:
   ```bash
   python3 tools/csas_gold/get_gold_price.py --json
   ```
4. If necessary, I can query a specific product by its direct notation ID using the `--notation` or `-n` parameter (e.g., `F74258118`).
5. After obtaining the data, I will present the prices clearly to the user, strictly adhering to their preferred language (Czech), formatting, and currency display.
6. Whenever I provide data from this API, I must cite the sources correctly using the IEEE format.

## Sources I must cite

When providing information from this skill, I must use my IEEE citation skill and include these sources:
[1] Investicní centrum (Česká spořitelna). "Zlaté slitky." Investicnicentrum.cz. [Online]. Available: https://www.investicnicentrum.cz/cs/produkty/zlate-slitky.
[2] Erste Group. MIG GraphQL endpoint (cz-mdp). [Online]. Available: https://mig.erstegroup.com/gql/cz-mdp/.