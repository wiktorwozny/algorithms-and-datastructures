from zad7ktesty import runtests
from collections import deque


def bfs(T, x0, y0):
    Q = deque()
    Q.append((1, y0))

    while Q:
        u = Q.popleft()
        if not (u[0] == x0 and u[1] == y0):
            T[x0][y0] += T[u[0]][u[1]]
            T[u[0]][u[1]] = 0
            if u[0] - 1 >= 0 and T[u[0] - 1][u[1]] != 0:
                Q.append((u[0] - 1, u[1]))
            if u[0] + 1 < len(T) and T[u[0] + 1][u[1]] != 0:
                Q.append((u[0] + 1, u[1]))
            if u[1] - 1 >= 0 and T[u[0]][u[1] - 1] != 0:
                Q.append((u[0], u[1] - 1))
            if u[1] + 1 < len(T[0]) and T[u[0]][u[1] + 1] != 0:
                Q.append((u[0], u[1] + 1))


# def f(P, Z, i, l, DP):
#
#     if DP[i][l] != -1:
#         return DP[i][l]
#
#     if i == 0 or l == 0:
#         return 0
#
#     if P[i - 1] <= l:
#         DP[i][l] = max(f(P, Z, i - 1, l, DP), f(P, Z, i - 1, l - P[i - 1], DP) + Z[i - 1])
#         return DP[i][l]
#     else:
#         DP[i][l] = f(P, Z, i - 1, l, DP)
#         return DP[i][l]
#
#
# def ogrodnik(T, D, Z, L):
#
#     P = []
#     for i in D:
#         bfs(T, 0, i)
#         P.append(T[0][i])
#
#     n = len(P)
#     DP = [[-1 for l in range(L + 1)] for i in range(n + 1)]
#
#     f(P, Z, n, L, DP)
#
#     for i in range(len(DP)):
#         print(DP[i])
#
#     print(Z[-1])
#     return max(DP[n])

def ogrodnik(T, D, Z, L):

    P = []
    for i in D:
        bfs(T, 0, i)
        P.append(T[0][i])

    n = len(P)
    DP = [[0 for l in range(L + 1)] for i in range(n)]

    for l in range(P[0], L + 1):
        DP[0][l] = Z[0]

    for l in range(L + 1):
        for i in range(1, n):
            DP[i][l] = DP[i - 1][l]
            if l - P[i] >= 0:
                DP[i][l] = max(DP[i][l], DP[i - 1][l - P[i]] + Z[i])

    return DP[n - 1][L]


runtests(ogrodnik, all_tests=True)
