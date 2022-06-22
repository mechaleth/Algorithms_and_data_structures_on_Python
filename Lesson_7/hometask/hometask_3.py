# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#  Примечание: задачу можно решить без сортировки исходного массива.
#  Но если это слишком сложно, используйте метод сортировки,
#  который не рассматривался на уроках (сортировка слиянием также недопустима).

import random
from test_sorts import test_sort

MINIMUM = 32


def find_minrun(n):
    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        element = array[i]
        j = i - 1
        while element < array[j] and j >= left:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    return array


def merge(array, l, m, r):
    array_length1 = m - l + 1
    array_length2 = r - m
    left = []
    right = []
    for i in range(0, array_length1):
        left.append(array[l + i])
    for i in range(0, array_length2):
        right.append(array[m + 1 + i])

    i = 0
    j = 0
    k = l

    while j < array_length2 and i < array_length1:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = right[j]
            j += 1

        k += 1

    while i < array_length1:
        array[k] = left[i]
        k += 1
        i += 1

    while j < array_length2:
        array[k] = right[j]
        k += 1
        j += 1


def tim_sort(array):
    n = len(array)
    minrun = find_minrun(n)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(array, start, end)

    size = minrun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            merge(array, left, mid, right)

        size = 2 * size


test_sort(tim_sort)

m = 10
minimum = -100
maximum = 100

size = 2 * m + 1
array = [random.randint(minimum, maximum - 1) for _ in range(size)]
# random.shuffle(array)
print(f'origin array:\n{array}')
tim_sort(array)
print(f'sorted array:\n{array}')

print(f'medium is {array[len(array) // 2]}')
