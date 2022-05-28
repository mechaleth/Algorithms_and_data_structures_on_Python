# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint

from math import inf


def two_min_search(array: list) -> tuple:
    if len(array) == 0:
        return None, None
    if len(array) == 1:
        return array[0], None

    min_1, min_2 = inf, inf

    for element in array:
        if element < min_1:
            min_1 = element

    if array.count(min_1) > 1:
        return min_1, min_1
    # В общем случае, массив не упорядочен
    # и без второй проходки не обойтись
    for element in array:
        if element < min_2 and element != min_1:
            min_2 = element

    return min_1, min_2


# параметры генерации случайных величин
array_size = randint(0, 25)
min_array_gen = -20
max_array_gen = 20

array = [randint(min_array_gen, max_array_gen) for _ in range(array_size)]

print(array)
print("Минимальными значениями являются {0}, {1}".format(*two_min_search(array)))
