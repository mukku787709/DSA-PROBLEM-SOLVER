import pytest
from solver import solve_problem


def test_sorting_dispatch():
    text = "Sort the array of integers"
    res = solve_problem(text)
    assert "code" in res and "explanation" in res
    assert "merge_sort" in res["code"] or "sort" in res["explanation"].lower()


def test_searching_dispatch():
    text = "Given a sorted array, find target using binary search"
    res = solve_problem(text)
    assert "binary_search" in res["code"]


def test_dp_dispatch():
    text = "Compute fibonacci number"
    res = solve_problem(text)
    assert "fib_dp" in res["code"]


def test_graph_dispatch():
    text = "Use BFS to traverse the graph"
    res = solve_problem(text)
    assert "bfs" in res["code"]
