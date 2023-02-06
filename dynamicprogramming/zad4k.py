from zad4ktesty import runtests


def f(row, col, T, DP):

    if DP[row][col] is not None:
        return DP[row][col]

    min_val = 10**100

    if row - 1 >= 0:
        min_val = min(min_val, f(row - 1, col, T, DP))
    if col - 1 >= 0:
        min_val = min(min_val, f(row, col - 1, T, DP))

    DP[row][col] = min_val + T[row][col]
    return DP[row][col]


def falisz(T):

    n = len(T)
    DP = [[None for y in range(n)] for x in range(n)]

    DP[0][0] = 0

    x = f(n - 1, n - 1, T, DP)
    ans = []
    i, j = n - 1, n - 1
    while i > 0 and j > 0:
        w1 = f(i - 1, j, T, DP)
        w2 = f(i, j - 1, T, DP)
        if w1 < w2:
            i -= 1
        else:
            j -= 1
        ans.append((i, j))

    if i == 0:
        j -= 1
        while j > 0:
            ans.append((0, j))
            j -= 1
    else:
        i -= 1
        while i > 0:
            ans.append((i, 0))
            i -= 1

    ans.append((0, 0))
    asd = 0
    for j, d in ans:
        asd += T[j][d]
    print(asd)

    return x


# def falisz(T):
#
#     n = len(T)
#
#     DP = [[0 for y in range(n)] for x in range(n)]
#     DP[0][0] = 0
#
#     for row in range(n):
#         for col in range(n):
#             if row == 0 and col == 0:
#                 continue
#             val = 10**100
#             if col - 1 >= 0:
#                 val = min(val, DP[row][col - 1])
#             if row - 1 >= 0:
#                 val = min(val, DP[row - 1][col])
#
#             DP[row][col] = val + T[row][col]
#
#     return DP[n - 1][n - 1]


runtests(falisz)
