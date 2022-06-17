# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и
# 	определить программы с наиболее эффективным использованием памяти.
# 	Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
#
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
#    проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с
# кодом.
#    Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
#    Надеемся, что вы не испортили программы, добавив в них множество `sys.getsizeof` после каждой переменной,
#    а проявили творчество, фантазию и создали универсальный код для замера памяти.

# Определить, какое число в массиве встречается чаще всего.
from random import randint
import sys


def get_most_frequent_1(array: list) -> tuple:
    """
    Возвращает самый часто встречающийся элемент и его частоту
    :param array: список или кортеж
    :return: кортеж с элементом и частотой
    """
    if not (isinstance(array, list) or isinstance(array, tuple)):
        raise TypeError("Expected array is list or tuple")

    max_count_element, max_count = None, 0
    set_array = set(array)

    # краеугольный камень!
    print(f"Общий размер краеугольных элементов {get_most_frequent_1.__name__}: "
          f"{sys.getsizeof(set_array) + sys.getsizeof(array)}")

    for element in set_array:
        element_count = array.count(element)
        if element_count > max_count:
            max_count, max_count_element = element_count, element
    return max_count_element, max_count



def get_most_frequent_2(array: list) -> tuple:
    """
    Возвращает самый часто встречающийся элемент    и его частоту
    :param array: список или кортеж
    :return: кортеж с элементом и частотой
    """
    max_freq = 0
    element = array[0]
    elements = dict()
    for item in array:
        if item in elements.keys():
            elements[item] += 1
        else:
            elements[item] = 1
        new_freq = elements[item]
        if new_freq > max_freq:
            max_freq = new_freq
            element = item

    # краеугольный камень!
    print(f"Общий размер краеугольных элементов {get_most_frequent_2.__name__}: "
          f"{sys.getsizeof(elements) + sys.getsizeof(array)}")

    return element, elements[element]

def get_most_frequent_3(array: list) -> tuple:
    """
    Возвращает самый часто встречающийся элемент    и его частоту
    :param array: список или кортеж
    :return: кортеж с элементом и частотой
    """
    max_freq = 1
    max_freq_element = array[0]
    array_size = len(array)
    for index in range(array_size):
        countage = 1
        for i in range(index + 1, array_size):
            if array[index] == array[i]:
                countage += 1
        if countage > max_freq:
            max_freq = countage
            max_freq_element = array[index]

    # краеугольный камень!
    print(f"Общий размер краеугольных элементов {get_most_frequent_3.__name__}: "
          f"{sys.getsizeof(array)}")

    return max_freq_element, max_freq

# параметры генерации случайных величин
array_size = 1000# randint(0, 25)
min_array_gen = -10000
max_array_gen = 10000

array = [randint(min_array_gen, max_array_gen) for _ in range(array_size)]


# print(sys.version, sys.platform)
# 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] win32

# Общий размер краеугольных элементов get_most_frequent_1: 41840
# преобразование в set займёт O(N)
# На самом деле, O(N * M), так как не каждый элемент листа туда попадёт.
# Но в худшем случае, O(N * N).

# timeit 100 элементов 1000 loops, best of 5: 256 usec per loop
# timeit 900 элементов 1000 loops, best of 5: 25.4 msec per loop
get_most_frequent_1(array)
# Самый неоптимальный вариант - нет решающего выигрыша ни по скорости,
# ни по объёму используемой памяти

#Общий размер краеугольных элементов get_most_frequent_2: 45816
# O(N), только один цикл
# timeit 100 элементов 1000 loops, best of 5: 42.4 usec per loop
# timeit 900 элементов 1000 loops, best of 5: 408 usec per loop
get_most_frequent_2(array)
# Для современных устройств оптимальный вариант

# Общий размер краеугольных элементов get_most_frequent_3: 8856
# Реализация с двойным циклом O(N*N)
# timeit 100 элементов 1000 loops, best of 5: 704 usec per loop
# timeit 900 элементов 100 loops, best of 5: 62.5 msec per loop
get_most_frequent_3(array)
# Более медленный и экономичный вариант
# Самый медленный из всех, на огромном количестве
# элементов, несмотря на экономию памяти, сомнителен из-за скорости