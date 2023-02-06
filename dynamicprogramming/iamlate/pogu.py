from zad3testy import runtests
from math import inf, isinf


def rec(T, V, q, left, idx, DP):

    if left < 0:
        return inf

    if idx == len(T) - 1:
        return 0

    if DP[idx][left] is not None:
        return DP[idx][left]

    distance = T[idx + 1] - T[idx]

    if distance > left:  # wymuszone tankowanie
        if left + V[idx] > q:
            newleft = q
        else:
            newleft = left + V[idx]

        w1 = rec(T, V, q, newleft - distance, idx + 1, DP) + 1
        DP[idx][left] = w1
        return DP[idx][left]

    else:
        w1 = rec(T, V, q, left - distance, idx + 1, DP)  # nie tankuje

        if left + V[idx] > q:
            newleft = q
        else:
            newleft = left + V[idx]
        w2 = rec(T, V, q, newleft - distance, idx + 1, DP) + 1  # tankuje choc nie musze

        DP[idx][left] = min(w1, w2)
        return DP[idx][left]


def iamlate(T, V, q, l):

    T.append(l)
    V.append(0)
    n = len(T)

    DP = [[None for _ in range(q + 1)] for _ in range(n)]

    x = rec(T, V, q, 0, 0, DP)
    if isinf(x):
        return []

    ans = []
    idx = 0
    left = 0

    while idx < len(T) - 1:
        distance = T[idx + 1] - T[idx]

        if distance > left:
            ans.append(idx)
            if left + V[idx] > q:
                newleft = q
            else:
                newleft = left + V[idx]

            left = newleft - distance

        else:
            w1 = rec(T, V, q, left - distance, idx + 1, DP)

            if left + V[idx] > q:
                newleft = q
            else:
                newleft = left + V[idx]
            w2 = rec(T, V, q, newleft - distance, idx + 1, DP) + 1

            if w1 < w2:
                left -= distance
            else:
                ans.append(idx)
                left = newleft - distance

        idx += 1

    return ans


runtests(iamlate)
