# Матрица 5x4 заполняется вводом с клавиатуры,
# кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

def get_number_by_string(string_number: str):
    """
    Функция преобразования строки к какому-либо числовому формату

    :param string_number: число в строковом виде
    :return: число в числовом формате
    """
    try:
        return int(string_number)
    except ValueError:
        # если и тут ошибка, пробрасываем во внешний код
        return float(string_number)


# try:
#     matrix = [[get_number_by_string(input(f"введите {i + 1} числовой элемент {j + 1} строки матрицы: "))
#                for i in range(4)]
#               for j in range(5)]
# except ValueError:
#     print("Uncorrect element type - expected int or float. Sorry")
#     quit()

# Так у пользователя есть шанс исправиться
rows = 5
columns = 4
matrix = [[] for _ in range(rows)]

# Заполняем 3 из 4 столбцов
for j, row in enumerate(matrix, 1):
    i = 1
    while i < columns:
        try:
            row.append(get_number_by_string(
                input(f"введите {i} числовой элемент {j} строки матрицы: ")))
            i += 1
        except ValueError:
            print("Uncorrect element type - expected int or float. Try again")

# заполняем последний столбец
for row in matrix:
    row_sum = 0
    for element in row:
        row_sum += element
    row.append(row_sum)

# печать матрицы
for row in matrix:
    for element in row:
        print(f'{element:>8}', end='')
    print()
