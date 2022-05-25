# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# Начало
# max_sum = 0
# max_sum_number = 0
max_sum = 0
max_sum_number = 0
# Цикл[^1] с постусловием
while True:
    # Вывод сообщения: "Введите натуральное число. Для выхода введите любую строку"
    # Ввод строки input_string
    input_string = input("Введите натуральное число. Для выхода введите любую строку ")
    # Если input_string не число, то:
    if not input_string.isnumeric():
        # __выход из цикла[^1]__
        break
    # Преобразование input_string в число num
    num = int(input_string)
    # summ = 0
    # integer = num
    summ, integer = 0, num
    # Цикл[^2] integer !=  0
    while integer != 0:
        # Находим остаток remainder и целое integer от деления operate_num на 10
        integer, remainder = divmod(integer, 10)
        # summ += remainder
        summ += remainder
    # Если sum > max_sum
    if summ > max_sum:
        # max_sum = summ
        # max_sum_number = num
        max_sum = summ
        max_sum_number = num
# Вывод числа max_sum_number и суммы его чисел max_sum
print(f'Число {max_sum_number} имеет наибольшую сумму {max_sum}')
# Конец
