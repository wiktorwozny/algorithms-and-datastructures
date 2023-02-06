from math import inf


def mayweather(G):  # postac krawedziowa

    n = 0
    for i in range(len(G)):
        n = max(n, G[i][0], G[i][1])

    n += 1

    distances = [[inf] * n for _ in range(n)]
    next = [[None] * n for _ in range(n)]
    for i in range(len(G)):
        distances[G[i][0]][G[i][1]] = G[i][2]
        next[G[i][0]][G[i][1]] = G[i][1]

    for i in range(n):
        distances[i][i] = 0
        next[i][i] = i

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if distances[j][k] > distances[j][i] + distances[i][k]:
                    distances[j][k] = distances[j][i] + distances[i][k]
                    next[j][k] = next[j][i]

    # for i in range(n):
    #     print(distances[i])

    return distances, next


def floyd(G):

    distances, next = mayweather(G)

    path = [8]
    u = 0
    v = 8
    while u != v:
        u = next[u][v]
        path.append(u)

    return path


graph = [[0,1,1],[0,7,2],[1,0,1],[1,2,2],[1,4,3],[2,1,2],[2,3,5],[3,2,5],[3,6,1],[4,1,3],[4,5,3],[4,7,1],[5,4,3],
        [5,6,8],[5,8,1],[6,3,1],[6,5,8],[6,8,4],[7,0,2],[7,4,1],[7,8,7],[8,5,1],[8,6,4],[8,7,7]]

print(floyd(graph))
