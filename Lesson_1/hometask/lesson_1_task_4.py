# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

# Начало
# Ввод двух букв symb_1 и symb_2
symb_1 = input("Введите букву a-z ")
symb_2 = input("Введите букву a-z ")
# Определение кодов ASCII code_1 и code_2 для symb_1 и symb_2 соответсвенно
code_1, code_2 = ord(symb_1), ord(symb_2)
# Определение кода ASCII code_a для символа "a"
code_a = ord('a')
# Вывод code_1 - code_a и code_2 - code_a
print(f"Символ {symb_1} расположен на позиции {code_1 - code_a + 1}")
print(f"Символ {symb_2} расположен на позиции {code_2 - code_a + 1}")
# Если code_1 > code_2, то:
if code_1 > code_2:
    #  Вывод code_1 - code_2
    print(f"Между символами {symb_2} и {symb_1} расположено {code_1 - code_2} символов")
# Иначе:
else:
    # Вывод code_2 - code_1
    print(f"Между символами {symb_1} и {symb_2} расположено {code_2 - code_1} символов")
# Конец
