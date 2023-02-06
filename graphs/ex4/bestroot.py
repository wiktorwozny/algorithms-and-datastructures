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


def best_root(L):

    n = len(L)

    K = []
    for u in range(n):
        for v in L[u]:
            K.append([u, v, 1])

    distances, _ = mayweather(K)

    ans = -1
    minii = inf
    for u in range(n):
        x = max(distances[u])
        if x < minii:
            minii = x
            ans = u

    return ans


graph = [[2],
         [2],
         [0, 1, 3],
         [2, 4],
         [3, 5, 6],
         [4],
         [4]]


print(best_root(graph))

