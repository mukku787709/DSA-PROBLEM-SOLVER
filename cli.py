import sys
from solver.dispatcher import solve_problem


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: python cli.py \"<problem description>\"")
        return
    problem_text = " ".join(argv)
    result = solve_problem(problem_text)
    print("--- Explanation ---")
    print(result.get("explanation"))
    print()
    print("--- Complexity ---")
    print(result.get("complexity"))
    print()
    print("--- Example Code (Python) ---")
    print(result.get("code"))


if __name__ == "__main__":
    main()
