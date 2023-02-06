def tasks(T):

    n = len(T)
    graph = [[0] * n for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if T[u][v] == 1:
                graph[u][v] = 1
            elif T[u][v] == 2:
                graph[v][u] = 1

    visited = [False] * n
    path = []

    for u in range(n):
        if not visited[u]:
            dfsvisit(graph, u, visited, path)

    return path[::-1]


def dfsvisit(G, u, visited, path):

    visited[u] = True
    for v in range(len(G)):
        if G[u][v] and not visited[v]:
            dfsvisit(G, v, visited, path)

    path.append(u)


T = [[0, 2, 1, 1], [1, 0, 1, 1], [2, 2, 0, 1], [2, 2, 2, 0]]
print(tasks(T))
