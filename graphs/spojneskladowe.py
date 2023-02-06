def dfs(G):

    time = 0

    def dfsvisit(G, u, visited, parents, times):

        nonlocal time
        # time += 1
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                dfsvisit(G, v, visited, parents, times)

        time += 1  # wierzcholek u przetworzony, time ma czas przetworzenia
        times[u] = time

    n = len(G)
    visited = [False] * n
    parents = [None] * n

    times = [0] * n

    time = 0

    for u in range(n):
        if not visited[u]:
            dfsvisit(G, u, visited, parents, times)

    return times


def skladowe(G):

    n = len(G)

    times = dfs(G)
    new = [[] for _ in range(n)]

    # odwracanie krawedzi, tworze nowy graf
    for i in range(n):
        for v in G[i]:
            new[v].append(i)

    times2 = [[0, 0] for _ in range(n)]
    for i in range(n):
        times2[i][0] = times[i]
        times2[i][1] = i

    times2.sort(key=lambda x: x[0], reverse=True)

    visited = [False] * n
    counter = 0

    for i in range(n):
        if not visited[times2[i][1]]:
            dfsik(new, times2[i][1], visited)
            counter += 1

    return counter


def dfsik(G, u, visited):

    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            dfsik(G, v, visited)


graph = [[1, 4], [2], [0], [4, 6], [5], [3], [5], [8], [9], [5, 10], [7]]

print(skladowe(graph))
