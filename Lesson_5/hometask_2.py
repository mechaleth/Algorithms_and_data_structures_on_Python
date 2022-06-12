# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#
# Примечание:
# - Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
#   задача решается в несколько строк.
# 	- Для прокачки алгоритмического мышления такой вариант не подходит.
# 	- Поэтому использование встроенных функций для перевода из одной системы счисления в другую
# 	в данной задаче под запретом.
# 	- Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
import collections
import itertools

direct_dict = collections.ChainMap({str(i): i for i in range(10)},
                                   {char: i for i, char in enumerate("ABCDEF", 10)})
reverse_dict = collections.ChainMap({i: str(i) for i in range(10)},
                                    {i: char for i, char in enumerate("ABCDEF", 10)})


def get_16_number() -> str:
    # Отрицательные не тестируем, сорри
    while True:
        str_number = input("Введите неотрицательное шестнадцатеричное число (пример A1B) >>")
        if not set([i for i in str_number]).issubset(set(direct_dict)):
            print("Это не шестнадцатеричное число в требуемом формате!")
            continue
        return str_number


def sum_16(digit_1: str, digit_2: str) -> str:
    res = collections.deque()
    mem = 0
    for num_1, num_2 in itertools.zip_longest([n for n in digit_1[-1::-1]],
                                              [n for n in digit_2[-1::-1]], fillvalue='0'):
        dig = direct_dict[num_1] + direct_dict[num_2] + mem
        mem, integer = divmod(dig, 16)
        res.appendleft(reverse_dict[integer])
    if mem:
        res.appendleft(reverse_dict[mem])
    return ''.join(res)


def mult_16(digit_1: str, digit_2: str) -> str:
    inter = []
    mem = 0
    dig_1 = [n for n in digit_1[-1::-1]]
    for level, num_2 in enumerate([n for n in digit_2[-1::-1]], 0):
        spam = collections.deque()
        for num_1 in dig_1:
            dig = direct_dict[num_1] * direct_dict[num_2] + mem
            mem, integer = divmod(dig, 16)
            spam.appendleft(reverse_dict[integer])
        if mem:
            spam.appendleft(reverse_dict[mem])
            mem = 0
        # на каждом этапе сохранияем текущее значение
        # с учётом разряда для итогового сложения столбиком
        spam.extend(tuple('0' for _ in range(level)))
        inter.append(''.join(spam))

    cur_res = inter[0]
    for dig in inter[1:]:
        cur_res = sum_16(dig, cur_res)

    return cur_res


dig_1 = get_16_number()
dig_2 = get_16_number()

print(f"{dig_1} + {dig_2} = {sum_16(dig_1, dig_2)}")
print(f"{dig_2} + {dig_1} = {sum_16(dig_2, dig_1)}")
print(f"{dig_1} * {dig_2} = {mult_16(dig_1, dig_2)}")
print(f"{dig_2} * {dig_1} = {mult_16(dig_2, dig_1)}")
