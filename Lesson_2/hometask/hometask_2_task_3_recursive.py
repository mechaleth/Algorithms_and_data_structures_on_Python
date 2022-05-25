# Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# get_inverse(current_integer, current_inverse)
def get_inverse(current_integer, current_inverse):
    # Если current_integer == 0:
    if current_integer <= 0:
        return current_inverse
    # Находим целое current_integer и остаток remainder от деления current_integer на 10
    current_integer, remainder = divmod(current_integer, 10)
    return get_inverse(current_integer, current_inverse * 10 + remainder)
# Конец


# Начало
# Ввод целого неотрицательного числа num
num = int(input("Введите целое неотрицательное число num: "))
new_num = get_inverse(num, 0)
# Вывод num и new_num
print(f"Исходное число {num}, получившееся число {new_num}")
# Конец
