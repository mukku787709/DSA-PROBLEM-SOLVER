# DSA Problem Solver Agent

This is a small, extensible Python-based DSA Problem Solver agent (MVP).
It accepts a problem description and uses simple keyword heuristics to pick an algorithm module, then returns an explanation, example code (Python), and complexity notes.

Purpose: provide a starting point you can extend with more problem parsing, additional algorithms, or ML components.

Quick start

1. Ensure you have Python 3.8+ installed.
2. From the project root, run tests:

```powershell
python -m pytest -q
```

3. Try the CLI with an example problem:

```powershell
python cli.py "Given a sorted array, find if target exists using binary search"
```

Files
- `cli.py`: command-line entry.
- `solver/dispatcher.py`: simple problem analyzer and router.
- `solver/algorithms/*`: algorithm modules that produce solution text and code.
- `tests/test_solver.py`: basic tests.

Next steps
- Add more algorithms and better problem parsing.
- Integrate with an LLM for advanced parsing and code generation.
- Add unit tests for each algorithm's code output.
