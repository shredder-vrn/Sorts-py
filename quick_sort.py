# Глобальные переменные для подсчёта операций
comparison_count = 0
swap_count = 0


def partition(arr, left, right):
    global comparison_count, swap_count

    # Выбираем первый элемент как опорный
    pivot = arr[left]
    i = left
    j = right + 1

    while True:
        # Сдвигаем указатель j влево, пока не найдем элемент <= pivot
        while True:
            j -= 1
            comparison_count += 1  # Увеличиваем счётчик сравнений
            if arr[j] <= pivot:
                break

        # Сдвигаем указатель i вправо, пока не найдем элемент >= pivot
        while True:
            i += 1
            comparison_count += 1  # Увеличиваем счётчик сравнений
            if i > right or arr[i] >= pivot:
                break

        # Если указатели пересеклись, выходим из цикла
        if i >= j:
            break

        # Меняем местами arr[i] и arr[j]
        arr[i], arr[j] = arr[j], arr[i]
        swap_count += 1  # Увеличиваем счётчик перестановок

    # Размещаем опорный элемент на его правильное место
    arr[left], arr[j] = arr[j], arr[left]
    swap_count += 1  # Увеличиваем счётчик перестановок

    # Возвращаем индекс опорного элемента
    return j


def quick_sort(arr, left, right):
    if left < right:
        # Выполняем разбиение
        pivot_index = partition(arr, left, right)

        # Рекурсивно сортируем левую и правую части
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)


# Пример использования
arr = [18, 2, 12, 15, 4, 20, 10, 13, 7, 3, 19, 5, 11, 1, 6, 8, 14, 16, 9, 17]


print("Неотсортированный массив:")
print(arr)

# Сортировка
quick_sort(arr, 0, len(arr) - 1)

# Вывод отсортированного массива
print("Отсортированный массив:")
print(arr)

# Вывод количества операций
print(f"Количество сравнений: {comparison_count}")
