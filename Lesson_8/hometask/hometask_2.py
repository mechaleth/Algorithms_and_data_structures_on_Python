# Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

from collections import deque

graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkrsta(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = {i: deque() for i in range(len(graph))}
    parent[start].append(start)

    cost[start] = 0
    min_cost = 0
    root = start

    while min_cost < float('inf'):

        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                # if parent[start]:
                #     if parent[i]:
                #         if parent[0] != root:
                #             parent[i].extend(parent[start])
                parent[i].append(start)
                vertex_cost = vertex + cost[start]
                if cost[i] > vertex_cost:
                    cost[i] = vertex_cost

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for key, deq in parent.items():
        if key not in deq and bool(deq):
            parent[key].append(key)

    for key, deq in parent.items():
        way_wander(parent, root, key)

    return (cost, parent)


def way_wander(parent: dict, root, element):
    """
    dict of graph deque optimizator
    :param parent: dict of graph deque
    :param root: base node
    :param element: current node
    :return: None
    """
    if element == root:
        return
    queue = parent[element]
    if not queue:
        return
    first_element = queue[0]
    if first_element == root:
        return
    else:
        queue.popleft()
        way_wander(parent, root, first_element)
        for i in range(len(parent[first_element]) - 1, -1, -1):
            queue.appendleft(parent[first_element][i])
        return


s = int(input("начальная вершина "))
lists = dijkrsta(graph, s)
print(lists[0])
print(f'Список вершин для обхода {lists[1]}')
