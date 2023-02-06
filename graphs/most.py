def dfs(G):  # nie wiem jak to jest z przetworzonymi wierzcholkami czy musze miec ten warunek zeby patrzec na low
    # krawedzi wstecznych

    time = 0

    def dfsvisit(G, u, visited, parents, times, low):

        nonlocal time
        time += 1
        visited[u] = True
        times[u] = time
        low[u] = time

        for v in G[u]:

            if visited[v] and parents[u] != v:
                low[u] = min(low[u], low[v])

            if not visited[v]:
                parents[v] = u
                dfsvisit(G, v, visited, parents, times, low)
                low[u] = min(low[u], low[v])

    n = len(G)
    low = [None] * n
    visited = [False] * n
    parents = [None] * n

    times = [0] * n

    time = 0

    for u in range(n):
        if not visited[u]:
            dfsvisit(G, u, visited, parents, times, low)

    bridges = []

    for i in range(n):
        if low[i] == times[i]:
            if parents[i] is None:
                continue
            bridges.append((parents[i], i))

    return bridges


# a - 0, b - 1, c - 2, d- 3, e - 4, f - 5, g- 6
graph = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 5], [2], [3, 6, 7], [5, 7], [5, 6]]

print(dfs(graph))
