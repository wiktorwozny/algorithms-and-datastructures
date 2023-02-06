from zad9ktesty import runtests
from math import inf


def f(P, i, l1, l2, DP):

    if i == len(P):
        return 0

    if DP[i][l1][l2] is not None:
        return DP[i][l1][l2]

    if P[i] > l1 and P[i] > l2:
        return 0

    if P[i] > l1:
        DP[i][l1][l2] = f(P, i + 1, l1, l2 - P[i], DP) + 1
        return DP[i][l1][l2]
    elif P[i] > l2:
        DP[i][l1][l2] = f(P, i + 1, l1 - P[i], l2, DP) + 1
        return DP[i][l1][l2]
    else:
        case1 = f(P, i + 1, l1, l2 - P[i], DP)
        case2 = f(P, i + 1, l1 - P[i], l2, DP)
        DP[i][l1][l2] = max(case1, case2) + 1
        return DP[i][l1][l2]


def prom(P, g, d):

    n = len(P)
    DP = [[[None for l2 in range(d + 1)] for l1 in range(g + 1)] for i in range(n)]

    x = f(P, 0, g, d, DP)

    i = 0
    sol1 = []
    sol2 = []
    while i < n and (g >= P[i] or d >= P[i]):
        if P[i] > g:
            w1 = 0
            w2 = 1
        elif P[i] > d:
            w1 = 1
            w2 = 0
        else:
            w1 = f(P, i + 1, g - P[i], d, DP)
            w2 = f(P, i + 1, g, d - P[i], DP)

        if w1 > w2:
            sol1.append(i)
            g -= P[i]
        else:
            sol2.append(i)
            d -= P[i]

        i += 1

    if x - 1 in sol1:
        return sol1
    else:
        return sol2


runtests(prom)
