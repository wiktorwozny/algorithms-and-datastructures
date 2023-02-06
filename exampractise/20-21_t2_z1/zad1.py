from zad1testy import runtests
from collections import deque

counter = 0


def rec(I, x, y, idx, DP):

    if I[idx][1] == y:
        DP[idx] = True
        return True

    if I[idx][1] > y:
        return False

    if DP[idx] is not None:
        return DP[idx]

    flag = False
    for i in range(idx + 1, len(I)):
        if I[idx][1] == I[i][0]:
            res = rec(I, x, y, i, DP)
            if res:
                flag = True
        if I[i][0] > I[idx][1]:
            break

    DP[idx] = flag
    return flag


def intuse(I, x, y):

    print(len(I))

    n = len(I)
    copy = []
    for i in range(n):
        copy.append((I[i][0], I[i][1], i))

    copy.sort()

    DP = [None for _ in range(n)]

    for i in range(n):
        if copy[i][0] == x:
            rec(copy, x, y, i, DP)
        if copy[i][0] > x:
            break

    ans = []
    for i in range(n):
        if DP[i]:
            ans.append(copy[i][2])

    return sorted(ans)


# def intuse(I, x, y):  # grafowo
#
#     n = len(I)
#     G = {}
#
#     for i, x, y in enumerate(I):
#         if x in G:
#             G[x].append(y)
#         else:
#             G[x] = [y]
#
#     # jebac to nie umiem slownikow


runtests(intuse)
