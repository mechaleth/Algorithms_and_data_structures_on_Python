# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# функция расчёта
import sys

# Последовательности 1..n

def get_sequence_element(el_num):
    return ((-1) ** (el_num-1)) / (2 ** (el_num-1))


# Итерационная часть
def get_iteration_sum(num):
    summ = 0
    # Цикл по i от 1 до num+1:
    for i in range(1, num+1):
        summ += get_sequence_element(i)
    return summ


# Рекурсивная часть
def get_recursive_sum(el_num):
    if el_num <= 1:
        return get_sequence_element(el_num)
    return get_sequence_element(el_num) + get_recursive_sum(el_num - 1)


if __name__ == "__main__":
    # Основная часть
    # Начало
    # Ввод неотрицательного целого n
    n = int(input("Введите целый неотрицательный лимит последовательности: "))
    # sum_n = 0
    pre_stack = 1
    # Если n >= максимальной глубины стека - pre_stack:
    # На самом деле, корректнее посчитать сумму как для 50,
    # так как ряд сходится...Но мы делаем, как делаем.
    if n >= sys.getrecursionlimit() - pre_stack:
        # sum_n = get_iteration_sum(n)
        print(f"Сумма {n} элементов последовательности получена итеративно и равна {get_iteration_sum(n)}")
    # Иначе:
    else:
        print(f"Сумма {n} элементов последовательности получена рекурсивно и равна {get_recursive_sum(n)}")
    # sum_n = get_recursive_sum(n)
    # Вывод sum_n
    # Конец
