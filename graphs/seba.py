from math import inf


def warshall(G, n):  # postac krawedziowa

    distances = [[inf] * n for _ in range(n)]
    for i in range(len(G)):
        distances[G[i][0]][G[i][1]] = G[i][2]

    for i in range(n):
        distances[i][i] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if distances[j][k] > distances[j][i] + distances[i][k]:
                    distances[j][k] = distances[j][i] + distances[i][k]

    return distances


def centrum(G, L):

    n = len(G)
    K = []
    for u in range(n):  # zamieniam na postac krawedziowa
        for v in range(n):
            if G[u][v] < 1000000:
                K.append([u, v, G[u][v]])

    distances = warshall(K, n)

    ans = None
    minimum = inf
    for u in range(n):
        curr = 0
        for v in L:
            curr += distances[u][v]

        if curr < minimum:
            minimum = curr
            ans = u

    return ans

