from math import inf
from queue import PriorityQueue

from zad2testy import runtests


def robot(L, A, B):
    G = makeGraph(L)

    # 0 - dół 1 - prawo 2 - góra 3 - lewo
    # 0 - 45 1 - 60 2 - 40 3 - 30

    a = len(L) * A[0] + A[1]
    b = B[1] + B[0] * len(L)
    d = dijkstra(G, a, b, len(L))

    return d


def dijkstra(G, a, b, n):
    d = [[[inf for _ in range(len(G))] for _ in range(4)] for _ in range(4)]
    visited = [[[False for _ in range(len(G))] for _ in range(4)] for _ in range(4)]
    parents = [[[-1 for _ in range(len(G))] for _ in range(4)] for _ in range(4)]
    q = PriorityQueue()

    # 0 - dół 1 - prawo 2 - góra 3 - lewo
    # 0 - 45 1 - 60 2 - 40 3 - 30
    # speed, turn, u
    d[0][1][a] = 0
    q.put((0, a, 1, 0))

    while not q.empty():
        dis, u, turn, speed = q.get()

        if u == b:
            return dis

        for v in G[u]:
            x_u = u % n
            y_u = u // n
            x_v = v % n
            y_v = v // n

            sideToGo = 0

            if x_v > x_u:
                sideToGo = 0
            elif x_v < x_u:
                sideToGo = 2
            elif y_v > y_u:
                sideToGo = 1
            elif y_v < y_u:
                sideToGo = 3

            val = 0
            newSpeed = speed
            if turn == sideToGo:
                if speed < 3: newSpeed += 1
            else:
                val = 45
                newSpeed = 1

            value = 45
            if newSpeed == 1:
                value = 60
            elif newSpeed == 2:
                value = 40
            elif newSpeed == 3:
                value = 30
            value += val

            if not visited[newSpeed][sideToGo][v]:
                if d[newSpeed][sideToGo][v] > dis + value:
                    d[newSpeed][sideToGo][v] = dis + value
                    parents[newSpeed][sideToGo][v] = u
                    q.put((dis + value, v, sideToGo, newSpeed))

        visited[speed][turn][u] = True

    return None


def makeGraph(L):
    G = [[] for _ in range(len(L) * len(L[0]))]
    n = len(L)

    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == ' ':
                if i + 1 < len(L) and L[i + 1][j] == ' ':
                    G[i + j * n].append(i + 1 + j * n)
                if i - 1 >= 0 and L[i - 1][j] == ' ':
                    G[i + j * n].append(i - 1 + j * n)
                if j + 1 < len(L[i]) and L[i][j + 1] == ' ':
                    G[i + j * n].append(i + (j + 1) * n)
                if j - 1 >= 0 and L[i][j - 1] == ' ':
                    G[i + j * n].append(i + (j - 1) * n)

    return G


runtests(robot)
