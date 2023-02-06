from zad3testy import runtests


def intersect(p1, p2):

    a, b = p1
    c, d = p2

    if a >= c and b <= d:
        return a, b

    if c >= a and d <= b:
        return c, d

    if a < c < b < d:
        return c, b

    if c < a < d < b:
        return a, d

    return 0, 0


def rec(A, K, idx, DP):

    if idx == len(A):
        return 0, 0

    if K == 0:
        return A[idx]

    if DP[idx][K] is not None:
        return DP[idx][K]

    maxsize = 0
    maxrange = (0, 0)
    for i in range(idx + 1, len(A)):
        inter = intersect(A[idx], rec(A, K - 1, i, DP))
        if inter[1] - inter[0] > maxsize:
            maxsize = inter[1] - inter[0]
            maxrange = inter

    DP[idx][K] = maxrange
    return maxrange


def kintersect(A, k):

    n = len(A)
    DP = [[None for _ in range(k + 1)] for _ in range(n)]

    bescik = -1
    for i in range(n - k + 1):
        inter = rec(A, k - 1, i, DP)
        bescik = max(bescik, inter[1] - inter[0])

    print(bescik)

    return []


runtests(kintersect)
