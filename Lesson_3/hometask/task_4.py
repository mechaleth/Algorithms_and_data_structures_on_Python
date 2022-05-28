# Определить, какое число в массиве встречается чаще всего.
from random import randint


def get_most_frequent(array: list) -> tuple:
    """
    Возвращает самый часто встречающийся элемент
    и его частоту

    :param array: список или кортеж
    :return: кортеж с элементом и частотой
    """
    if not (isinstance(array, list) or isinstance(array, tuple)):
        raise TypeError("Expected array is list or tuple")
    max_count_element, max_count = None, 0
    for element in set(array):
        element_count = array.count(element)
        if element_count > max_count:
            max_count, max_count_element = element_count, element
    return max_count_element, max_count


# параметры генерации случайных величин
array_size = randint(0, 25)
min_array_gen = -20
max_array_gen = 20

array = [randint(min_array_gen, max_array_gen) for _ in range(array_size)]

most_frequent, frequency = get_most_frequent(array)

message = "не найден" \
    if most_frequent is None \
    else f"{most_frequent} с частотой {frequency}"

print(array)
print(f"Самый часто встречаемый элемент {message}")
