from collections import deque


def bfs(G, s):

    n = len(G)
    visited = [False] * n
    distances = [0] * n
    parents = [None] * n
    queue = deque()
    visited[s] = True
    queue.append(s)

    while queue:
        u = queue.popleft()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distances[v] = distances[u] + 1
                parents[v] = u
                queue.append(v)

    return distances, parents


def packages(G, towns):

    n = len(G)

    while True:

        wyjebane = 0
        for u in range(n):
            if len(G[u]) == 1 and u not in towns:
                wyjebane += 1
                G[G[u][0]].remove(u)
                G[u].pop()

        if wyjebane == 0:
            break

    distances, parents = bfs(G, towns[0])
    maxdis = 0
    maxind = -1
    for i in range(n):
        if distances[i] > maxdis:
            maxdis = distances[i]
            maxind = i

    distances, parents = bfs(G, maxind)

    maxdis = 0
    maxind = -1
    for i in range(n):
        if distances[i] > maxdis:
            maxdis = distances[i]
            maxind = i

    path = []

    while maxind is not None:
        path.append(maxind)
        maxind = parents[maxind]

    poza = []
    for i in range(n):
        if len(G[i]) != 0 and i not in path:
            poza.append(i)

    return len(path) + 2 * len(poza) - 1



graph = [
    [1],
    [0,2],
    [1,3,4,6],
    [2],
    [2,5],
    [4],
    [2,7,8,10],
    [6],
    [6,9],
    [8],
    [6,11],
    [10]
    ]

miasta = [0, 4, 5, 6, 7, 11]

print(packages(graph, miasta))
