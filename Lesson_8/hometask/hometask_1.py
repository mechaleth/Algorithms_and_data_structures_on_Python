# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям
# (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

friends_count = 0
while True:
    try:
        friends_count = int(input("Введите количество друзей >>>"))
    except Exception:
        continue
    if friends_count >= 0:
        break

# формируем матрицу смежности
# можно было бы использовать ориентированный граф,
# но процесс рукопожатия взаимный, все связи двухнаправленные
adjency_matrix = [[] for _ in range(friends_count)]
for vertex, edges in enumerate(adjency_matrix, 0):
    for node in range(friends_count):
        # человек не здоровается сам с собой
        if vertex != node:
            edges.append(1)
        else:
            edges.append(0)

# print(adjency_matrix)

# считаем количество рукопожатий
count = 0
# список ручкающихся)
associate_list = []

for vertex, edges in enumerate(adjency_matrix):
    associate_list.append(vertex)
    for node, edge in enumerate(edges):
        if node in associate_list:
            continue
        count += edge

print(f'Для {friends_count} друзей {count} рукопожатий')