def solve_problem(text: str):
    explanation = (
        "This looks like a searching problem on a (possibly) sorted array. We'll provide Binary Search and notes.\n"
        "Binary search works on sorted arrays by halving the search interval each step."
    )
    code = '''def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# example usage
if __name__ == "__main__":
    print(binary_search([1,2,3,4,5], 3))
'''
    complexity = "Time: O(log n); Space: O(1)."
    return {"explanation": explanation, "code": code, "complexity": complexity}
