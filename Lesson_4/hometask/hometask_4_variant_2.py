# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# 		Второй — без использования «Решета Эратосфена».
# 		Примечание. Вспомните классический способ проверки числа на простоту.
# 		Пример работы программ:
#
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2
import itertools
import cProfile


def test_it(func):
    simple_nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i, num in enumerate(simple_nums, 1):
        if func(i) == num:
            print("OK")
        else:
            print("Not OK")


def get_simple(num: int) -> int:
    assert num > 0, "num must be a positive!"
    counter = 0
    for number in itertools.count(1):
        div_check = False
        for number_ in range(2, int(number ** 0.5) + 1):
            if number % number_ == 0:
                div_check = True
                break
        if div_check:
            continue
        counter += 1
        if counter >= num:
            return number

# test_it(get_simple)

# Сложность алгоритма O(N**1.5)

# cProfile.run('get_simple(100)')
# 4 function calls in 0.001 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 hometask_4_variant_2.py:30(get_simple)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# python -m timeit -n 1000 -s "import hometask_4_variant_2 as task" "task.get_simple(100)"
# 1000 loops, best of 5: 781 usec per loop

# cProfile.run('get_simple(1000)')
# 4 function calls in 0.032 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.032    0.032 <string>:1(<module>)
#         1    0.032    0.032    0.032    0.032 hometask_4_variant_2.py:30(get_simple)
#         1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# python -m timeit -n 100 -s "import hometask_4_variant_2 as task" "task.get_simple(1000)"
# 100 loops, best of 5: 20.4 msec per loop
