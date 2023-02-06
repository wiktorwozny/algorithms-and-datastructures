from Exercise_1_tests import runtests
from math import inf
from queue import Queue


def bfs(graph, start):

    n = len(graph)
    parents = [None] * n
    visited = [False] * n
    queue = Queue()

    visited[start] = True
    queue.put(start)

    while not queue.empty:
        u = queue.get()

        for v in range(n):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parents[v] = u
                queue.put(v)

    return parents


def floydwarshall(G):

    n = len(G)
    distances = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            elif G[i][j] != 0:
                distances[i][j] = G[i][j]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                distances[j][k] = min(distances[j][k], distances[j][i] + distances[i][k])

    return distances


def keep_distance(M, x, y, d):

    n = len(M)
    size = n * n

    distances = floydwarshall(M)

    graph = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(n):
        for j in range(n):
            if i != j or distances[i][j] > d:
                for u in range(n):
                    for v in range(n):
                        if distances[u][v] < d or (u == j and i == v):
                            continue

                        if (i == u and M[j][v] != 0) or (j == v and M[i][u] != 0) or (M[i][u] != 0 and M[j][v] != 0):
                            graph[i * n + j][u * n + v] = 1

    start = x * n + y
    parents = bfs(graph, start)

    v = y * n + x
    res = []
    while v is not None:
        res.append((v // n, v % n))
        v = parents[v]

    res.reverse()
    # print(res)

    return res


M = [
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 1],
[0, 1, 1, 0],
]
x = 0
y = 3
d = 2

runtests(keep_distance)


