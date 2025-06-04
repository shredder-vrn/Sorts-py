def interpolation_search(arr, x):
    comparisons = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        pos = low + ((high - low) * (x - arr[low])) // (arr[high] - arr[low])

        comparisons += 1
        if arr[pos] == x:
            return pos, comparisons
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1


arr =  [1, 4, 6, 8, 9, 10, 13, 15, 19, 20, 25, 28, 30, 36, 39, 42, 47, 50, 51, 60]

total_comparisons = 0
for x in arr:
    index, comparisons = interpolation_search(arr, x)
    total_comparisons += comparisons
print(len(arr))
print(total_comparisons/len(arr))
