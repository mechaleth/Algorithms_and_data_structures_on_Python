# Определить, является ли год, который
# ввел пользователь, високосным или не високосным.

# Начало
# Ввод года year
year = int(input("Введите год, а мы скажем, високосный он или нет: "))
# Если year < 0:
if year < 0:
    # Вывод сообщения о том, что до нашей эры мы ничего не знаем/помним/лень
    print("До нашей эры была путаница, поэтому не знаем!")
# Если year % 100 == 0:
elif year % 100 == 0:
    # Если year % 400 == 0:
    if year % 400 == 0:
        # Вывод сообщения о том, что год високосный
        print(f"Год {year} високосный")
    # Иначе:
    else:
        # Вывод сообщения о том, что год не високосный
        print(f"Год {year} не високосный")
# Иначе если year % 4 == 0:
elif year % 4 == 0:
    # Вывод сообщения о том, что год високосный
    print(f"Год {year} високосый")
# Иначе
else:
    # Вывод сообщения о том, что год не високосный
    print(f"Год {year} не високосый")
# Конец