from collections import deque


def remove(G, u, v):

    for i in range(len(G[u])):
        if G[u][i] == v:
            G[u][i] = None
            break
    for i in range(len(G[v])):
        if G[v][i] == u:
            G[v][i] = None
            break


def euler(G):

    path = deque()
    dfs(G, 0, path)

    return path


def dfs(G, u, path):

    for v in G[u]:
        if v is not None:
            remove(G, u, v)
            dfs(G, v, path)

    path.appendleft(u)


# a - 0, b - 1, c - 2, d- 3, e - 4, f - 5
graph = [[1, 2], [0, 2, 3, 5], [0, 1, 3, 5], [1, 2, 4, 5], [3, 5], [1, 2, 3, 4]]

print(euler(graph))
