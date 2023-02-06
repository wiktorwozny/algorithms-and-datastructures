from queue import PriorityQueue as PQ
from math import inf


def islands(G, a, b):

    n = len(G)
    prices = [[inf] * 3 for _ in range(n)]
    visited = [[False] * 3 for _ in range(n)]
    queue = PQ()

    mapa1 = [1, 5, 8]
    mapa2 = [0, 0, 0, 0, 0, 1, 0, 0, 2]

    prices[a][0] = prices[a][1] = prices[a][2] = 0
    queue.put((0, a, 3))  # argument na indeksie dwa -> jak przyjechalismy mostem to jest 0,
    # jak przyjechalismy promem to 1, jak samolotem to 2

    while not queue.empty():
        p, u, jak = queue.get()

        if u == b:
            return p

        if jak == 3:
            for v in range(n):
                if G[u][v] == 1:
                    prices[v][0] = 1
                    queue.put((1, v, 0))

                if G[u][v] == 5:
                    prices[v][1] = 5
                    queue.put((5, v, 1))

                if G[u][v] == 8:
                    prices[v][2] = 8
                    queue.put((8, v, 2))

            visited[u][0] = visited[u][1] = visited[u][2] = True

        else:
            for v in range(n):
                if G[u][v] != 0 and not visited[v][mapa2[G[u][v]]]:
                    if G[u][v] != mapa1[jak]:
                        if prices[v][mapa2[G[u][v]]] > prices[u][jak] + G[u][v]:
                            prices[v][mapa2[G[u][v]]] = prices[u][jak] + G[u][v]
                            queue.put((p + G[u][v], v, mapa2[G[u][v]]))

            visited[u][jak] = True

    return None


G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]

print(islands(G1, 5, 2))
