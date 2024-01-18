import time

def binary_search(array, searched_value, first, last):
    if first > last:
        return -1  # элемент не найден

    middle = (first + last) // 2
    middle_value = array[middle]

    if middle_value == searched_value:
        return middle
    elif middle_value > searched_value:
        return binary_search(array, searched_value, first, middle - 1)
    else:
        return binary_search(array, searched_value, middle + 1, last)

def main():
    print("Бинарный поиск (рекурсивная реализация)")
    input_str = input("Введите элементы массива: ")
    array = list(map(int, input_str.split()))

    array.sort()
    print(f"Упорядоченный массив: {', '.join(map(str, array))}")

    while True:
        k = int(input("Введите искомое значение или -1000 для выхода: "))
        if k == -1000:
            break

        search_result = binary_search(array, k, 0, len(array) - 1)
        if search_result < 0:
            print(f"Элемент со значением {k} не найден")
        else:
            print(f"Элемент найден. Индекс элемента со значением {k} равен {search_result}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)