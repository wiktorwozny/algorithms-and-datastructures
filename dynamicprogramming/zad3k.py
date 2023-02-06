import sys

sys.setrecursionlimit(999999999)

from zad3ktesty import runtests
from math import inf


# def f(i, T, k, DP):
#
#     if DP[i] is not None:
#         return DP[i]
#
#     min_val = 10**100
#
#     for j in range(i - k, i):
#         min_val = min(min_val, f(j, T, k, DP) + T[i])
#
#     DP[i] = min_val
#     return DP[i]
#
#
# def ksuma(T, k):
#
#     n = len(T)
#     DP = [None for _ in range(n)]
#
#     for i in range(k):
#         DP[i] = T[i]
#
#     res = 10**100
#
#     for i in range(n - k, n):
#         res = min(res, f(i, T, k, DP))
#
#     ans = []
#
#     najidx = n
#     while najidx >= k:
#         naj = inf
#         for i in range(najidx - k, najidx):
#             if f(i, T, k, DP) < naj:
#                 naj = f(i, T, k, DP)
#                 najidx = i
#
#         ans.append(najidx)
#
#     # print(T)
#     # print(k)
#     # print(sorted(ans))
#     asd = 0
#     for i in range(len(ans)):
#         asd += T[ans[i]]
#     print(asd)
#
#     return res


# def rec(T, k, idx, ile, DP):
#
#     if idx == len(T):
#         return 0
#
#     if DP[idx][ile] is not None:
#         return DP[idx][ile]
#
#     if ile == 0:
#         w1 = rec(T, k, idx + 1, k - 1, DP) + T[idx]
#         DP[idx][ile] = w1
#         return DP[idx][ile]
#     else:
#         w1 = rec(T, k, idx + 1, ile - 1, DP)  # nie bieremy
#         w2 = rec(T, k, idx + 1, k - 1, DP) + T[idx]  # bieremy
#         DP[idx][ile] = min(w1, w2)
#         return DP[idx][ile]
#
#
# def ksuma(T, k):
#
#     n = len(T)
#     DP = [[None for _ in range(k)] for _ in range(n)]
#
#     x = rec(T, k, 0, k - 1, DP)
#
#     return x


def rec(T, k, idx, DP):

    if idx >= len(T):
        return 0

    if DP[idx] is not None:
        return DP[idx]

    mini = inf
    i = idx + 1
    while i <= idx + k:
        mini = min(mini, rec(T, k, i, DP))
        i += 1

    DP[idx] = mini + T[idx]
    return DP[idx]


def ksuma(T, k):

    n = len(T)
    DP = [None for _ in range(n)]

    for i in range(n - k, n):
        DP[i] = T[i]

    mini = inf
    for idx in range(k):
        mini = min(mini, rec(T, k, idx, DP))

    return mini


runtests(ksuma)
