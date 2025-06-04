def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    total_comparisons = 0  # Счётчик сравнений
    
    while swapped:
        swapped = False
        
        # Слева направо
        for i in range(start, end):
            total_comparisons += 1  # Увеличиваем количество сравнений
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if not swapped:
            break
        
        swapped = False
        end -= 1
        
        # Справа налево
        for i in range(end - 1, start - 1, -1):
            total_comparisons += 1  # Увеличиваем количество сравнений
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        
        start += 1

    return total_comparisons  # Возвращаем общее число сравнений

# Исходный массив
a = [19,17,15,13,11,9,7,5,3,1,20,18,16,14,12,10,8,6,4,2]


# Подсчёт сравнений
comparisons = cocktailSort(a)
print("Sorted array is:")
print(a)
print(f"Total comparisons: {comparisons}")
