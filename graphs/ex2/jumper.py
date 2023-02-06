from queue import PriorityQueue as PQ
from math import inf


def jumper(G, s, t):

    n = len(G)
    distances = [[inf] * 2 for _ in range(n)]
    visited = [[False] * 2 for _ in range(n)]
    queue = PQ()

    for i in range(2):
        distances[s][i] = 0

    queue.put((0, s, 0))
    while not queue.empty():
        d, u, warunek = queue.get()

        if u == t:
            return d

        for v in range(n):
            if G[u][v] != 0 and not visited[v][0]:
                if distances[v][0] > distances[u][warunek] + G[u][v]:
                    distances[v][0] = distances[u][warunek] + G[u][v]
                    queue.put((d + G[u][v], v, 0))
                if warunek == 0:
                    for w in range(n):
                        if G[v][w] != 0 and not visited[w][1]:
                            maksik = max(G[u][v], G[v][w])
                            if distances[w][1] > distances[u][warunek] + maksik:
                                distances[w][1] = distances[u][warunek] + maksik
                                queue.put((d + maksik, w, 1))

        visited[u][warunek] = True

    return None


graph = [[0, 1, 0, 0, 0],
         [1, 0, 1, 0, 0],
         [0, 1, 0, 7, 0],
         [0, 0, 7, 0, 8],
         [0, 0, 0, 8, 0]]

print(jumper(graph, 0, 4))
