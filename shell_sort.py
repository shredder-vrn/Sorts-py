import math

def generate_steps(n):
    """Generate step sequence h(s) for Shell sort."""
    steps = []
    h = 1
    while h < n:
        steps.append(h)
        h = 2 * h + 1  # h(s+1) = 2 * h(s) + 1
    print(steps)
    return steps[::-1] 

def shell_sort_with_comparisons(arr):
    n = len(arr)
    steps = generate_steps(n)
    comparisons = 0

    for gap in steps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap
            
            if j >= gap:
                comparisons += 1
            arr[j] = temp

    return comparisons

arr = [20,18,16,14,12,10,8,6,4,2,19,17,15,13,11,9,7,5,3,1]


comparisons = shell_sort_with_comparisons(arr)

print("Sorted array:", arr)
print("Total comparisons:", comparisons)
