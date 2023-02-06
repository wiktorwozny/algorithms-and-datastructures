from zad2ktesty import runtests


def f(a, b, S, DP):

    if DP[a][b] is not None:
        return DP[a][b]

    if a == b:
        return 1

    if a + 1 == b:
        if S[a] == S[b]:
            return 2
        return 0

    if S[a] != S[b]:
        DP[a][b] = 0
        return 0
    else:
        if f(a + 1, b - 1, S, DP) == 0:
            DP[a][b] = 0
            return 0
        else:
            DP[a][b] = f(a + 1, b - 1, S, DP) + 2
            return DP[a][b]


def palindrom(S):

    n = len(S)
    DP = [[None for b in range(n)] for a in range(n)]

    max_val = 0
    maxa = -1
    maxb = -1

    for a in range(n):
        for b in range(a + 1, n):
            x = f(a, b, S, DP)
            if x > max_val:
                max_val = x
                maxa = a
                maxb = b

    return S[maxa:maxb + 1]


runtests(palindrom)
