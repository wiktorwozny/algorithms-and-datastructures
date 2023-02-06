def dfs(G, visited, i, j, x, y):

    visited[i][j] = True
    if i - 1 >= 0 and G[i - 1][j] == 1:
        if not visited[i - 1][j]:
            dfs(G, visited, i - 1, j, x, y)
    if j + 1 < y and G[i][j + 1] == 1:
        if not visited[i][j + 1]:
            dfs(G, visited, i, j + 1, x, y)
    if i + 1 < x and G[i + 1][j]:
        if not visited[i + 1][j]:
            dfs(G, visited, i + 1, j, x, y)
    if j - 1 >= 0 and G[i][j - 1] == 1:
        if not visited[i][j - 1]:
            dfs(G, visited, i, j - 1, x, y)


def policz(G):

    x = len(G)
    y = len(G[0])
    ans = 0
    visited = [[False] * y for _ in range(x)]

    for i in range(x):
        for j in range(y):
            if G[i][j] == 1 and not visited[i][j]:
                dfs(G, visited, i, j, x, y)
                ans += 1

    return ans


graph = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        ]

print(policz(graph))
