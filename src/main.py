from random import randint
from typing import List


def transpose_array(array: List[List[int]]) -> List[List[int]]:
    return list(map(list, zip(*array)))


def print_array(array: List[List]) -> None:
    for string in array:
        print(*string)


def change_max_of_each_row_to_its_additive_inverse(array: List[List[int]]) -> None:
    print('-' * 50)
    print('\nЗадание: "1. Заменить максимальный элемент каждой строки на противоположный по знаку"\n')
    print('-' * 50)
    print('\nИсходные данные:\n')
    print_array(array)
    print()

    for row in array:
        indices = [index for index, item in enumerate(row) if item == max(row)]
        for index in indices:
            row[index] = -row[index]
    
    print('-' * 50)
    print('\nРешение задачи:\n')
    print_array(array)
    print()
    print('-' * 50)


def insert_zero_column_after_each_column_containing_max_array_element(array: List[List[int]]) -> None:
    print('-' * 50)
    print('\nЗадание: "2. Вставить после всех столбцов, содержащих максимальный элемент массива, столбец из нулей"\n')
    print('-' * 50)
    print('\nИсходные данные:\n')
    print_array(array)
    print()

    max_element = max(map(max, array))
    transposed_array = transpose_array(array)
    for column in transposed_array:
        if max_element in column:
            transposed_array.insert(
                transposed_array.index(column) + 1,
                [0 for _ in range(len(array))]
            )

    print('-' * 50)
    print('\nРешение задачи:\n')
    print_array(transpose_array(transposed_array))
    print()
    print('-' * 50)


def remove_columns_containing_negative_element(array: List[List[int]]) -> None:
    print('-' * 50)
    print('\nЗадание: "3. Удалить все столбцы, в которых есть отрицательный элемент"\n')
    print('-' * 50)
    print('\nИсходные данные:\n')
    print_array(array)
    print()

    transposed_array = transpose_array(array)
    temp = transposed_array.copy()
    for column in temp:
        for element in column:
            if element < 0:
                transposed_array.remove(column)
                break
    
    print('-' * 50)
    print('\nРешение задачи:\n')
    if transpose_array(transposed_array):
        print_array(transpose_array(transposed_array))
    else:
        print('Массив пуст')
    print()
    print('-' * 50)


def swap_first_and_last_columns(array: List[List[int]]) -> None:
    print('-' * 50)
    print('\nЗадание: "4. Поменять местами первый и последний столбцы"\n')
    print('-' * 50)
    print('\nИсходные данные:\n')
    print_array(array)
    print()

    transposed_array = transpose_array(array)
    transposed_array[0], transposed_array[-1] = transposed_array[-1], transposed_array[0]
    
    print('-' * 50)
    print('\nРешение задачи:\n')
    print_array(transpose_array(transposed_array))
    print()
    print('-' * 50)


def get_array() -> List[List[int]]:
    while True:
        rows = input('\nВведите количество строк массива (положительное число):\n')
        try:
            rows = int(rows)
            if rows < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print('\nОшибка ввода')
    
    while True:
        columns = input('\nВведите количество столбцов массива (положительное число):\n')
        try:
            columns = int(columns)
            if columns < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print('\nОшибка ввода')

    array = [[randint(-1000, 1000) for _ in range(columns)] for _ in range(rows)]
    return array


def main() -> None:
    actions = {
        "0": ("Выйти",),
        "1": ("Заменить максимальный элемент каждой строки на противоположный по знаку", change_max_of_each_row_to_its_additive_inverse) ,
        "2": ("Вставить после всех столбцов, содержащих максимальный элемент массива, столбей из нулей", insert_zero_column_after_each_column_containing_max_array_element),
        "3": ("Удалить все столбцы, в которых есть отрицательный элемент", remove_columns_containing_negative_element),
        "4": ("Поменять местами первый и последний столбцы", swap_first_and_last_columns),
    }

    for key, value in actions.items():
        print(f"{key}: {value[0]}")

    msg = "\nВведите желаемое действие:\n"
    while (action := input(msg).strip()) != "0":
        if action not in actions:
            print("\nОшибка ввода\n")
            for key, value in actions.items():
                print(f"{key}. {value[0]}")
        else:
            array = get_array()
            print()
            actions[action][1](array)

            print()
            for key, value in actions.items():
                print(f"{key}: {value[0]}")


if __name__ == '__main__':
    main()
