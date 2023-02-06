from math import inf


def intersect(o1, o2):
    p1 = o1
    p2 = o2
    if p1[0] == p2[0]:
        if p1[1] > p2[1]:
            p1 = o2
            p2 = o1
    if p1[0] > p2[0]:
        p1 = o2
        p2 = o1

    if p2[0] > p1[1]:
        return (0, 0)

    if p2[0] <= p1[1]:
        if p2[1] <= p1[1]:
            return (p2[0], p2[1])
        return (p2[0], p1[1])
    return (p2[0], p1[1])


def f(DP, A, k, i):
    if k == 1:
        return A[i]

    if i < k - 1:
        return (0, 0)

    if DP[i][k] != None:
        return DP[i][k]

    maxxsize = 0
    maxxrange = (0, 0)
    for j in range(i):
        inter = intersect(A[i], f(DP, A, k - 1, j))
        if inter[1] - inter[0] > maxxsize:
            maxxsize = inter[1] - inter[0]
            maxxrange = inter

    DP[i][k] = maxxrange
    return maxxrange


def kintersect(A, k):
    k = k + 1
    A.append((-inf, inf))

    DP = [[None for _ in range(k + 1)] for _ in range(len(A))]

    print(f(DP, A, k, len(A) - 1))

    ranges = []
    kk = k
    ii = len(A) - 1

    while kk != 1:
        maxxsize = 0
        selj = 0
        for j in range(ii):
            inter = intersect(A[ii], f(DP, A, kk - 1, j))
            if inter[1] - inter[0] > maxxsize:
                maxxsize = inter[1] - inter[0]
                selj = j

        if not selj in ranges:
            ranges.append(selj)
        ii = selj
        kk -= 1

    return ranges


from zad3testy import runtests

runtests(kintersect)