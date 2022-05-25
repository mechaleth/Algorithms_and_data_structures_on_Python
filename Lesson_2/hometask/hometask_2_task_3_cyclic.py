# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# Начало
# Ввод целого неотрицательного числа num
num = int(input("Введите целое неотрицательное число num: "))
new_num, integer = 0, num
# Цикл c условием integer>=0
while integer >= 0:
    # Нахождение целого integer и остатка remainder от деления integer на 10
    integer, remainder = divmod(integer, 10)
    new_num = new_num * 10 + remainder
# Вывод num и new_num
print(f"Исходное число {num}, получившееся число {new_num}")
# Конец
