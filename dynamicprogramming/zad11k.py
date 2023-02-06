from zad11ktesty import runtests


def f(T, dystr, i, p, DP):

    if i == len(T) - 1:
        DP[i][p] = abs(p - (dystr[len(T) - 1] - p))
        return abs(p - (dystr[len(T) - 1] - p))

    if DP[i][p] is not None:
        return DP[i][p]

    w1 = f(T, dystr, i + 1, p + T[i], DP)
    w2 = f(T, dystr, i + 1, p, DP)

    DP[i][p] = DP[i][dystr[len(T) - 1] - p] = min(w1, w2)
    return DP[i][p]


def kontenerowiec(T):

    n = len(T)
    dystr = [0] * n
    dystr[0] = T[0]

    for i in range(n):
        dystr[i] = T[i]

    for i in range(1, n):
        dystr[i] += dystr[i - 1]

    S = dystr[n - 1]

    DP = [[None for _ in range(S + 1)] for _ in range(n)]

    x = f(T, dystr, 0, 0, DP)

    # x = 10**100
    # for i in range(S + 1):
    #     if DP[n - 1][i] is not None and DP[n - 1][i] < x:
    #         x = DP[n - 1][i]

    return x


runtests(kontenerowiec)
    