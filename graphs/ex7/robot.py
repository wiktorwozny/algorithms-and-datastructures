from queue import PriorityQueue as PQ
from math import inf


def robot(L, A, B):

    rows = len(L)
    cols = len(L[0])

    visited = [[[[False] * 4 for _ in range(4)] for _ in range(cols)] for _ in range(rows)]
    distances = [[[[inf] * 4 for _ in range(4)] for _ in range(cols)] for _ in range(rows)]
    queue = PQ()

    y, x = A

    for i in range(4):
        distances[x][y][1][i] = 0

    queue.put((0, A, 0, 1))  # distance, point, movement, rotation
    # movement : 0 - was standing, 1 - 60s, 2 - 40s, 3 - 30s
    # rotation: 0 - up, 1 - right, 2 - down, 3 - left

    while not queue.empty():

        d, P, m, r = queue.get()
        y, x = P

        if P == B:
            return d

        if r == 0:
            if L[x - 1][y] == 'X':
                if not visited[x][y][0][1]:
                    if distances[x][y][0][1] > distances[x][y][m][r] + 45:
                        distances[x][y][0][1] = distances[x][y][m][r] + 45
                        queue.put((distances[x][y][m][r] + 45, P, 0, 1))  # hdwp jd


