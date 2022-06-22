# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random
from test_sorts import test_sort


def merge(array, left_index, right_index, middle):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle + 1:right_index + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_array_sort(array):
    def merge_sort(array, left_index, right_index):
        if left_index >= right_index:
            return

        middle = (left_index + right_index) // 2
        merge_sort(array, left_index, middle)
        merge_sort(array, middle + 1, right_index)
        merge(array, left_index, right_index, middle)

    merge_sort(array, 0, len(array) - 1)


test_sort(merge_array_sort)

size = 7  # 10
minimum = 0
maximum = 50
array = [random.randint(minimum, maximum - 1) for _ in range(size)]
# random.shuffle(array)
print(f'origin array:\n{array}')

merge_array_sort(array)
print(f'sorted array:\n{array}')
