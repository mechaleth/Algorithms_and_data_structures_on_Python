# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# функция расчёта
import sys

# Последовательности 1..n

import cProfile
from functools import lru_cache


def get_sequence_element(el_num):
    return (-1 if el_num % 2 == 0 else 1) / (2 ** (el_num - 1))


# Итерационная часть
def get_iteration_sum(num):
    item = 1
    summ = 0
    # Цикл по i от 1 до num+1:
    for i in range(num):
        summ += item
        item /= - 2
    return summ

# O(N)

# cProfile.run('get_iteration_sum(10)')
# 4 function calls in 0.000 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 hometask_2_task_4_1.py:19(get_iteration_sum)

# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_iteration_sum(10)"
# 1000 loops, best of 5: 2.39 usec per loop

# cProfile.run('get_iteration_sum(100)')
# 4 function calls in 0.000 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.000    0.001    0.000 hometask_2_task_4_1.py:19(get_iteration_sum)

# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_iteration_sum(100)"
# 1000 loops, best of 5: 18.2 usec per loop

# cProfile.run('get_iteration_sum(500)')
#   4 function calls in 0.000 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.000    0.001    0.000 hometask_2_task_4_1.py:19(get_iteration_sum)

# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_iteration_sum(500)"
# 1000 loops, best of 5: 92.7 usec per loop

# cProfile.run('get_iteration_sum(990)')
# 4 function calls in 0.000 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 hometask_2_task_4_1.py:19(get_iteration_sum)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_iteration_sum(990)"
# 1000 loops, best of 5: 187 usec per loop

# cProfile.run('get_iteration_sum(5000)')
# 4 function calls in 0.001 seconds

#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       1    0.001    0.001    0.001    0.001 hometask_2_task_4_1.py:19(get_iteration_sum)
#       1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_iteration_sum(5000)"
# 1000 loops, best of 5: 986 usec per loop

# Рекурсивная часть
# в данном исполнении, lry_cache не даёт никаких преимуществ
# только если в цикле запускаем. Много раз. Но тогда проще использовать готовый массив.
# Оптимизация направлена на сокращение стека вызова функций
# Из-за особенностей задачи рекурсивный вариант неоптимален.
# @lru_cache()
def get_recursive_sum(el_num):
    if el_num <= 1:
        return (-1 if el_num % 2 == 0 else 1) / (2 ** (el_num - 1))
    return (1 if el_num % 2 == 0 else -1) / (2 ** (el_num - 1)) + get_recursive_sum(el_num - 1)

# O(log(N))

# cProfile.run('get_recursive_sum(10)')
# 13 function calls (4 primitive calls) in 0.000 seconds

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       10    0.000    0.000    0.000    0.000 hometask_2_task_4_origin.py:12(get_sequence_element)
#     10/1    0.000    0.000    0.000    0.000 hometask_2_task_4_origin.py:66(get_recursive_sum)
# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_recursive_sum(10)"
# 1000 loops, best of 5: 12.4 usec per loop


# cProfile.run('get_recursive_sum(300)')
# 603 function calls (304 primitive calls) in 0.002 seconds

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      300    0.001    0.000    0.001    0.000 hometask_2_task_4_origin.py:12(get_sequence_element)
#    300/1    0.001    0.000    0.002    0.002 hometask_2_task_4_origin.py:66(get_recursive_sum)
# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_recursive_sum(100)"
# 1000 loops, best of 5: 170 usec per loop


# cProfile.run('get_recursive_sum(500)')
# 1003 function calls (504 primitive calls) in 0.004 seconds

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#      500    0.002    0.000    0.002    0.000 hometask_2_task_4_origin.py:12(get_sequence_element)
#    500/1    0.002    0.000    0.004    0.004 hometask_2_task_4_origin.py:66(get_recursive_sum)
# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_recursive_sum(500)"
# 1000 loops, best of 5: 1.22 msec per loop

# cProfile.run('get_recursive_sum(990)')
# 1983 function calls (994 primitive calls) in 0.008 seconds

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#      990    0.004    0.000    0.004    0.000 hometask_2_task_4_origin.py:12(get_sequence_element)
#    990/1    0.004    0.000    0.007    0.007 hometask_2_task_4_origin.py:66(get_recursive_sum)
#        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_recursive_sum(990)"
# 1000 loops, best of 5: 2.94 msec per loop









# python -m timeit -n 1000 -s "import hometask_2_task_4_origin as task_4" "task_4.get_recursive_sum(1000)"
# RecursionError: maximum recursion depth exceeded in comparison

# if __name__ == "__main__":
# Основная часть
# Начало
# Ввод неотрицательного целого n
#    n = int(input("Введите целый неотрицательный лимит последовательности: "))
# sum_n = 0
#    pre_stack = 1
# Если n >= максимальной глубины стека - pre_stack:
# На самом деле, корректнее посчитать сумму как для 50,
# так как ряд сходится...Но мы делаем, как делаем.
#    if n >= sys.getrecursionlimit() - pre_stack:
# sum_n = get_iteration_sum(n)
#        print(f"Сумма {n} элементов последовательности получена итеративно и равна {get_iteration_sum(n)}")
# Иначе:
#    else:
#        print(f"Сумма {n} элементов последовательности получена рекурсивно и равна {get_recursive_sum(n)}")
# sum_n = get_recursive_sum(n)
# Вывод sum_n
# Конец
