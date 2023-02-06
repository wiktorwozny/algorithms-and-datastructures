from zad5ktesty import runtests


def f(A, a, b, DP):

    if DP[a][b] is not None:
        return DP[a][b]

    if a == b:
        DP[a][b] = (A[a], 0)
        return DP[a][b]

    if a + 1 == b:
        DP[a][b] = (max(A[a], A[b]), min(A[a], A[b]))
        return DP[a][b]

    if A[a] + f(A, a + 1, b, DP)[1] > A[b] + f(A, a, b - 1, DP)[1]:
        DP[a][b] = (f(A, a + 1, b, DP)[1] + A[a], f(A, a + 1, b, DP)[0])
        return DP[a][b]
    else:
        DP[a][b] = (f(A, a, b - 1, DP)[1] + A[b], f(A, a, b - 1, DP)[0])
        return DP[a][b]


def garek(A):

    n = len(A)
    DP = [[None for i in range(n)] for j in range(n)]

    x = f(A, 0, n - 1, DP)

    # for i in range(n):
    #     print(DP[i])
    #
    # input()

    return x[0]


runtests(garek)
