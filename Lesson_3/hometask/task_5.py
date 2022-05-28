# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# 	   Примечание к задаче: пожалуйста не путайте
#      «минимальный» и «максимальный отрицательный».
#      Это два абсолютно разных значения.
from math import inf
from random import randint
# массив может быть пустым!
# много элементов сложно проверять
array_size = randint(0, 20)

# Массив со случайными числами
array = [randint(-100, 100) for _ in range(array_size)]

max_min = -inf
max_min_index = -1

# так как массив не упорядочен, нужно проверить все элементы
for index, element in enumerate(array):
    if (element < 0) and (element > max_min):
        max_min = element
        max_min_index = index
print(f'Рассматриваемый массив {array}')
sad_message = "отсутствует, так как нет отрицательных значений в массиве"
print(f'Максимальное отрицательное значение '
      f'{f"{max_min}, индекс {max_min_index}" if max_min > -inf else sad_message}')
