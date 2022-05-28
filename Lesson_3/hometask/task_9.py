# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

# генерируем отдельно размерность по
# строке, от 2
# столбцу, от 2
row_size, column_size = randint(2, 10), randint(2, 10)

# заполняем матрицу
matrix = [[randint(-100, 100) for _ in range(column_size)] for _ in range(row_size)]

# массив с минимумами копируем из первой строки
min_value_array = matrix[0].copy()

# пройдёмся по остальным строкам
for row in matrix[1:]:
    for j, element in enumerate(row):
        if min_value_array[j] > element:
            min_value_array[j] = element

# найдем максимум минимума
max_min = min_value_array[0]
for element in min_value_array[1:]:
    if element > max_min:
        max_min = element

# печать матрицы
for row in matrix:
    for element in row:
        print(f'{element:>5}', end='')
    print()
print('*' * column_size * 5)
print(''.join((f'{element:>5}' for element in min_value_array)))
print('*' * column_size * 5)
print(f'maximum among minimum {max_min}')
