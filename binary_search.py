def binary_search(lst, target):

    local_count = 0
    left = 0
    right = len(lst) - 1
    result = 0

    while left <= right:
        middle = (left + right) // 2
        local_count += 1
        if lst[middle] < target:
            left = middle + 1
        elif lst[middle] == target:
            result = middle + 1
            break
        else:
            right = middle - 1

    return result, local_count


N = 25
lst = list(range(1, N + 1)) 
total_comparisons = 0

print("Сравнения для каждого элемента:")
for i in range(1, N + 1):  
    _, comparisons = binary_search(lst, i)
    total_comparisons += comparisons
    print(f"Элемент {i}: {comparisons} сравнений")

print(f"\nОбщая сумма всех сравнений: {total_comparisons}")
print(f"Среднее число сравнений для каждого элемента: {total_comparisons/N}\n")

