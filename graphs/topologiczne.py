from collections import deque


def topologysort(G):

    n = len(G)

    visited = [False] * n
    path = deque()

    for u in range(n):
        if not visited[u]:
            dfs(G, u, visited, path)

    return path


def dfs(G, u, visited, path):

    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            dfs(G, v, visited, path)

    path.appendleft(u)

# a - 0, b - 1, c - 2, d- 3, e - 4, f - 5, g- 6
graph = [[1, 2, 5], [2, 4], [], [], [3, 6], [4], []]

print(topologysort(graph))
