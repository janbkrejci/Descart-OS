---
name: math-calculations
description: Skill for performing simple and complex mathematical calculations using Python.
---

# Math Calculations Skill

This skill allows me to perform mathematical calculations of any complexity.

## Procedure

1. For simple arithmetic, I can compute the result directly if I am absolutely certain.
2. For complex mathematical calculations, equations, algebra, calculus, or large number computations, I must always write and execute a Python script in the `workspace/` directory using the `uv run --script` format (per the `script-dependencies` memory rule):
   ```python
   #!/usr/bin/env -S uv run --script
   #
   # /// script
   # requires-python = ">=3.12"
   # dependencies = ["numpy", "scipy", "sympy"]
   # ///
   ```
3. I will use standard Python built-ins like `math`, or advanced libraries such as `numpy`, `scipy`, or `sympy` as needed.
4. I will make the script executable with `chmod +x`, execute it via the `bash` tool, capture the output, and present the exact mathematical result to the user clearly.
