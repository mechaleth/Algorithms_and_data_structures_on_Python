# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# 		Пример работы программ:
#
# ```
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2
import functools
import itertools
import cProfile


def test_it(func):
    simple_nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i, num in enumerate(simple_nums, 1):
        if func(i) == num:
            print(f"{num} is OK")
        else:
            print("Not OK")


def get_simp(n):
    num_list = [i for i in range(n)]
    num_list[1] = 0
    for i in range(2, n):
        if num_list[i] != 0:
            j = i * 2

            while j < n:
                num_list[j] = 0
                j += i
    return [i for i in num_list if i != 0]


def get_simple(index):
    num_list = []

    def get_last_simp(n):
        if n == 1:
            return True
        for i in range(len(num_list), n + 1):
            num_list.append(i)
        num_list[1] = 0
        for i in range(2, n + 1):
            if num_list[i] == 0:
                continue
            j = i * 2

            while j < n + 1:
                num_list[j] = 0
                j += i
        return num_list[-1] != 0

    count = index
    for i in itertools.count(1):
        if get_last_simp(i):
            count -= 1
        if count == 0:
            return i

# test_it(get_simple)

# Сложность алгоритма O(N**3)

# print({indx: item for indx, item in enumerate(get_simp(1000), 1)})
# print(get_simp(1000))

# cProfile.run('get_simple(100)')
# 1573 function calls in 0.057 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.056    0.056 <string>:1(<module>)
#         1    0.000    0.000    0.056    0.056 hometask_4_variant_1.py:46(get_simple)
#       523    0.056    0.000    0.056    0.000 hometask_4_variant_1.py:49(get_last_simp)
#         1    0.000    0.000    0.057    0.057 {built-in method builtins.exec}
#       522    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       524    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# python -m timeit -n 1 -s "import hometask_4_variant_1 as task" "task.get_simple(100)"
# 1 loop, best of 5: 71.4 msec per loop

# cProfile.run('get_simple(1000)')
# 23725 function calls in 17.887 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   17.887   17.887 <string>:1(<module>)
#         1    0.028    0.028   17.887   17.887 hometask_4_variant_1.py:46(get_simple)
#      7907   17.851    0.002   17.859    0.002 hometask_4_variant_1.py:49(get_last_simp)
#         1    0.000    0.000   17.887   17.887 {built-in method builtins.exec}
#      7906    0.004    0.000    0.004    0.000 {built-in method builtins.len}
#      7908    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# python -m timeit -n 1 -s "import hometask_4_variant_1 as task" "task.get_simple(1000)"
# 1 loop, best of 5: 25.9 sec per loop