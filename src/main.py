def transpose_array(array):
    return list(map(list, zip(*array)))


def print_array(array):
    for string in array:
        print(*string)


def change_max_of_each_row_to_its_additive_inverse(array):
    for row in array:
        indices = [index for index, item in enumerate(row) if item == max(row)]
        for index in indices:
            row[index] = -row[index]
    return array


def insert_zero_column_after_each_column_containing_max_array_element(array):
    max_element = max(map(max, array))
    transposed_array = transpose_array(array)
    for column in transposed_array:
        if max_element in column:
            transposed_array.insert(
                transposed_array.index(column) + 1,
                [0 for _ in range(len(array))]
            )
    return transpose_array(transposed_array)


def remove_columns_containing_negative_element(array):
    transposed_array = transpose_array(array)
    temp = transposed_array.copy()
    for column in temp:
        for element in column:
            if element < 0:
                transposed_array.remove(column)
                break
    return transpose_array(transposed_array)


def swap_first_and_last_columns(array):
    transposed_array = transpose_array(array)
    transposed_array[0], transposed_array[-1] = transposed_array[-1], transposed_array[0]
    return transpose_array(transposed_array)


def main():
    pass


if __name__ == '__main__':
    main()
