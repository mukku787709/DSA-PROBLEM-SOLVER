"""Simple rule-based dispatcher to route problem descriptions to algorithm modules.
This is intentionally minimal — extend with better parsing or ML later.
"""
from typing import Dict
import re

from solver.algorithms import sorting, searching, dp, graphs

# Order matters: put more specific/smaller-scope patterns earlier (e.g., searching before generic 'sorted')
KEYWORD_MAP = [
    (re.compile(r"binary search|\bsearch\b|find if target|lower_bound|upper_bound", re.I), searching),
    (re.compile(r"\bsort\b|\bsorted\b|merge sort|quick sort|heap sort", re.I), sorting),
    (re.compile(r"fibonacci|knapsack|dp|dynamic programming|longest common subsequence|lcs", re.I), dp),
    (re.compile(r"bfs|dfs|graph|shortest path|dijkstra|connected component|topological", re.I), graphs),
]


def solve_problem(text: str) -> Dict[str, str]:
    """Analyze `text` and return a solution dict with keys: explanation, code, complexity.

    The dispatcher uses simple keyword matching. If nothing matches, it falls back to a general DP helper (safe default).
    """
    text = (text or "").strip()
    for pattern, module in KEYWORD_MAP:
        if pattern.search(text):
            return module.solve_problem(text)
    # fallback
    return dp.solve_problem(text)
