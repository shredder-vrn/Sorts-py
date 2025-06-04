def generate_pratt_steps(n):
    steps = []
    i, j = 0, 0
    while 2**i <= n/2:
        j = 0
        while 2**i * 3**j <= n/2:
            steps.append(2**i * 3**j)
            j += 1
        i += 1

    print(sorted(steps, reverse=True))
    return sorted(steps, reverse=True) 

def shell_sort_with_pratt(arr):
    n = len(arr)
    steps = generate_pratt_steps(n)
    comparisons = 0

    for gap in steps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                comparisons += 1
            if j >= gap:
                comparisons += 1 
            arr[j] = temp

    return comparisons

arr = [10,9,8,7,6,5,4,3,2,1]
print("Array before sorting:", arr)

comparisons = shell_sort_with_pratt(arr)

print("Array after sorting:", arr)
print("Total comparisons:", comparisons)
