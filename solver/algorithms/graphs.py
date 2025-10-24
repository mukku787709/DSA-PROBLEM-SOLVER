def solve_problem(text: str):
    explanation = (
        "Graph problem detected. We'll provide a BFS implementation for unweighted shortest path / connectivity tasks.\n"
        "BFS explores nodes in increasing distance order and is optimal for unweighted shortest paths."
    )
    code = '''from collections import deque

def bfs(graph, start):
    # graph: dict node -> list of neighbors
    visited = set()
    order = []
    q = deque([start])
    visited.add(start)
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order

# example usage
if __name__ == "__main__":
    g = {1:[2,3], 2:[4], 3:[], 4:[]}
    print(bfs(g, 1))
'''
    complexity = "BFS: Time O(V+E), Space O(V)."
    return {"explanation": explanation, "code": code, "complexity": complexity}
