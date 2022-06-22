# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас
# должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random
from test_sorts import test_sort


def bubble_origin(array):
    n = 1
    count = 0
    while n < len(array):
        for i in range(len(array) - n):
            count += 1
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    #        print(array)
    print(f'количество вовлечённых элементов {count}')


def bubble(array: list):
    n = 1
    count = 0
    left_border = 0
    right_border = len(array) - 1
    while right_border >= left_border:
        minimum_index, maximum_index = right_border, left_border
        for i in range(left_border, right_border):
            count += 1
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            if array[i] > array[maximum_index]:
                maximum_index = i
        if maximum_index == left_border:
            left_border += 1
        right_border -= 1
    #        print(array)
    print(f'количество вовлечённых элементов {count}')


test_sort(bubble, True)
test_sort(bubble_origin, True)


size = 7  # 10
minimum = -100
maximum = 100
array = [random.randint(minimum, maximum - 1) for _ in range(size)]
# random.shuffle(array)
print(f'origin array:\n{array}')

one_more_array = array.copy()
bubble(array)
print(f'sorted array:\n{array}')

bubble_origin(one_more_array)
print(one_more_array)
