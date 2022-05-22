# Вводятся три разных числа.
# Найти, какое из них является средним
# (больше одного, но меньше другого)

# Начало
# Ввод трёх чисел a, b, c
a = float(input("Введите число: "))
b = float(input("Введите ещё одно число: "))
c = float(input("Введите последнее число: "))
# mid = b
mid = b
# Если a < c:
if a < c:
    # min = a
    min = a
    # max = c
    max = c
# Иначе
else:
    # min = c
    min = c
    # max = a
    max = a
# Если mid > max:
if mid > max:
    # mid = max
    # Нас не интересует судьба min и max, только mid
    mid = max
# Иначе если mid < min:
elif mid < min:
    # mid = min
    mid = min
# Вывод mid
print(f"Средним из чисел {a}, {b}, {c} является {mid}")
# Конец
