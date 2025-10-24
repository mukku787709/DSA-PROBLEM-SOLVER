def solve_problem(text: str):
    explanation = (
        "This problem looks like a sorting problem. A stable, general-purpose solution is Merge Sort.\n"
        "We'll provide an example implementation and complexity notes."
    )
    code = '''def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# example usage
if __name__ == "__main__":
    print(merge_sort([5,2,9,1,5,6]))
'''
    complexity = "Time: O(n log n) average and worst; Space: O(n) for merges. Stable sort."
    return {"explanation": explanation, "code": code, "complexity": complexity}
