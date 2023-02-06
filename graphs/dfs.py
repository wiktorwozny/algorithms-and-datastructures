def dfs(G):

    time = 0

    def dfsvisit(G, u, visited, parents, times):

        nonlocal time
        time += 1
        visited[u] = True
        times[u] = time

        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                dfsvisit(G, v, visited, parents, times)

        # time += 1  # wierzcholek u przetworzony, time ma czas przetworzenia

    n = len(G)
    visited = [False] * n
    parents = [None] * n

    times = [0] * n

    time = 0

    for u in range(n):
        if not visited[u]:
            dfsvisit(G, u, visited, parents, times)

    return times


# a - 0, b - 1, c - 2, d- 3, e - 4, f - 5, g- 6
graph = [[1, 2, 5], [2, 4], [], [], [3, 6], [4], []]

print(dfs(graph))


# def dfs(G):
#
#     n = len(G)
#     visited = [False] * n
#     parents = [None] * n
#
#     times = [0] * n
#
#     time = 0
#
#     for u in range(n):
#         if not visited[u]:
#             dfsvisit(G, u, time + 1, visited, parents, times)
#
#     return times
#
#
# def dfsvisit(G, u, time, visited, parents, times):
#
#     # time += 1
#     visited[u] = True
#     times[u] = time
#
#     for v in G[u]:
#         if not visited[v]:
#             parents[v] = u
#             dfsvisit(G, v, time + 1, visited, parents, times)
#
#     # time += 1  # wierzcholek u przetworzony, time ma czas przetworzenia
#
#
# # a - 0, b - 1, c - 2, d- 3, e - 4, f - 5, g- 6
# graph = [[1, 2, 5], [2, 4], [], [], [3, 6], [4], []]
#
# print(dfs(graph))
