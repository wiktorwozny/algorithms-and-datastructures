from math import inf
from collections import deque


def bfs(G, s, t, parents):

    n = len(G)
    visited = [False] * n
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.popleft()
        for v in range(len(G[u])):
            if v != u and not visited[v] and G[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parents[v] = u
                if v == t:
                    return True

    return False


def fulkerson(G, source, sink):

    n = len(G)
    parents = [None for _ in range(n)]
    flow = 0

    while True:

        if not bfs(G, source, sink, parents):
            break

        path = 10**10
        s = sink
        while s != source:
            path = min(path, G[parents[s]][s])
            s = parents[s]

        flow += path

        v = sink
        while v != source:
            G[parents[v]][v] -= path
            G[v][parents[v]] += path
            v = parents[v]

    return flow


def mayweather(G):

    n = 0
    for i in range(len(G)):
        n = max(n, G[i][0], G[i][1])

    n += 1

    distances = [[inf] * n for _ in range(n)]

    for u, v, w in G:
        distances[u][v] = w

    for i in range(n):
        distances[i][i] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if distances[j][k] > distances[j][i] + distances[i][k]:
                    distances[j][k] = distances[j][i] + distances[i][k]

    return distances


def blueandgreen(G, C, d):

    n = len(G)
    K = []
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                K.append([u, v, G[u][v]])

    distances = mayweather(K)

    G2 = [[0] * (n + 2) for _ in range(n + 2)]

    for u in range(n):
        for v in range(u + 1, n):
            if distances[u][v] >= d:
                if C[u] == 'B' and C[v] == 'G':
                    G2[0][u + 1] = 1
                    G2[u + 1][v + 1] = 1
                    G2[v + 1][n + 1] = 1

                if C[u] == 'G' and C[v] == 'B':
                    G2[0][v + 1] = 1
                    G2[v + 1][u + 1] = 1
                    G2[u + 1][n + 1] = 1

    return fulkerson(G2, 0, n + 1)


T = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
C = ['B', 'B', 'G', 'G', 'B']
D = 2

print(blueandgreen(T, C, D))
