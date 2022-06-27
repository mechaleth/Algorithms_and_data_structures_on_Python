# Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# 		Примечания:
# 		a. граф должен храниться в виде списка смежности;
# 		b. генерация графа выполняется в отдельной функции,
# 	       которая принимает на вход число вершин.

# речь не идёт об оптимальном пути. Мы просто должны прийти в конец.

import random
from collections import deque


def graph_generate(N: int) -> list:
    """
    Generates unweighted oriented loopless graph
    as a adjacency list
    :param N: number of nodes
    :return: adjacency list
    """
    assert N >= 0, "Sorry, true graph has a non negative nodes count!"
    return [list(set([random.choice([i for i in range(N) if i != k]) for _ in range(N)])) for k in range(N)]


def dfs(graph: list, start: int, wish_end: int):
    """
    dfs function
    :param graph: current graph
    :param start: start node
    :param wish_end: finish node
    :return: way or none if not finish unreachable
    """

    def dfs_(graph: list, start: int, wish_end: int, is_visited: list, way: deque):
        if start == wish_end:
            is_visited[start] = True
            way.appendleft(start)
            return True
        if is_visited[start]:
            return False

        is_visited[start] = True
        # исследуем всех соседей(ближайшие соседние вершины)
        for neighbor in graph[start]:
            # если сосед не посещался
            if not is_visited[neighbor]:
                # двигаемся по пути и проверяем, не достигли ли мы пункта назначения
                reached = dfs_(graph, neighbor, wish_end, is_visited, way)
                # возвращаем true, если достигли
                if reached:
                    way.appendleft(start)
                    return True
        # если добраться невозможно
        return False

    is_visited = [False for _ in range(vertex_count)]
    way = deque()
    if dfs_(graph, start, wish_end, is_visited, way):
        return way
    else:
        return None


vertex_count = 0

while True:
    try:
        vertex_count = int(input("Введите количество вершин >>>"))
    except Exception:
        continue
    if vertex_count >= 0:
        break

graph = graph_generate(vertex_count)

print(graph)

start, finish = 0, vertex_count - 1
while True:
    try:
        start, finish = int(input("enter start vertex ")), int(input("enter finish vertex "))
    except Exception:
        continue
    if start < 0 or finish < 0:
        continue
    if start >= vertex_count or finish >= vertex_count:
        continue
    break

way = dfs(graph, start, finish)
way_interpret = "->".join(map(str, dfs(graph, start, finish)))\
    if way is not None else "doesn't exists"
print(f'dfs way from {start} to {finish} is {way_interpret}')