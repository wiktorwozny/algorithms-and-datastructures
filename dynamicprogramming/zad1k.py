from zad1ktesty import runtests


def val(S, x):
    if S[x] == "0":
        return 1
    return -1


def f(a, b, S, DP):

    if DP[a][b] is not None:
        return DP[a][b]

    DP[a][b] = f(a, b - 1, S, DP) + val(S, b)

    return DP[a][b]


def roznica(S):

    n = len(S)
    DP = [[None for b in range(n)] for a in range(n)]

    for x in range(n):
        DP[x][x] = val(S, x)

    max_val = -1

    for a in range(n):
        for b in range(a + 1, n):
            max_val = max(max_val, f(a, b, S, DP))

    return max_val


runtests(roznica)
