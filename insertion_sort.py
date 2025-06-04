def insertionSort(arr):
    n = len(arr)  # Длина массива
    comparisons = 0  # Счётчик сравнений

    if n <= 1:
        return comparisons  # Если массив состоит из одного элемента, сравнений нет

    for i in range(1, n):  # Проход по массиву
        key = arr[i]  # Текущий элемент для вставки
        j = i - 1

        # Перемещаем элементы, пока не найдём место для вставки
        while j >= 0:
            comparisons += 1  # Увеличиваем счётчик сравнений
            if key >= arr[j]:
                break
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Вставляем ключ в нужное место

    return comparisons  # Возвращаем общее количество сравнений

# Исходный массив
arr = [20,18,16,14,12,10,8,6,4,2,19,17,15,13,11,9,7,5,3,1]



# Сортируем массив и считаем сравнения
total_comparisons = insertionSort(arr)

# Вывод
print("Sorted array:", arr)
print("Total comparisons:", total_comparisons)
