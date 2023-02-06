E = [(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]

n = 7

G = [[] for _ in range(n)]

for u, v, w in E:
    G[u].append((v, w))
    G[v].append((u, w))

for i in range(len(G)):
    print(i, " ", G[i])

