# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

# Начало
# Ввод номера буквы в алфавите symbol_num
symbol_num = int(input("Введите целочисленный номер [1;26] буквы в алфавите a-z: "))
# Определение  ASCII кодов code_a и code_z для символов "a" и “z” соответственно
code_a, code_z = ord("a"), ord("z")
# Если symbol_num <= code_z - code_a + 1 и symbol_num > 0:
if (symbol_num <= code_z - code_a + 1) and (symbol_num > 0):
    # symbol_code = code_a + symbol_num - 1
    symbol_code = code_a + symbol_num - 1
    # Определение буквы symbol по коду ASCII
    symbol = chr(symbol_code)
    # Вывод symbol
    print(f"По номеру {symbol_num} в алфавите расположена буква {symbol}")
# Иначе
else:
    # Вывод сообщения об ошибочном номере буквы
    print(f"Номер символа {symbol_num} вне алфавита 'a' - 'z'")
# Конец
