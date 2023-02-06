from zad4testy import runtests


def a(T, x):
    return T[x][1]


def b(T, x):
    return T[x][2]


def h(T, x):
    return T[x][0]


def select_buildings(T, P):

    n = len(T)
    copy = [0] * n

    for i in range(n):
        copy[i] = T[i]

    T.sort(key=lambda tup: tup[2])
    # T.sort(key=lambda tup: tup[1])
    F = [[0 for p in range(P + 1)] for i in range(n)]

    for i in range(n):
        for p in range(T[i][3], P + 1):
            F[i][p] = (b(T, i) - a(T, i)) * h(T, i)

    for p in range(P + 1):
        for i in range(1, n):
            if F[i][p] != 0:
                to_add = 0
                for x in range(i):
                    if b(T, x) >= a(T, i):
                        break
                    to_add = max(to_add, F[x][p - T[i][3]])

                F[i][p] += to_add

    maxi = -1
    maxval = 0
    ans = []

    for i in range(n):
        if F[i][P] > maxval:
            maxi = i
            maxval = F[i][P]

    i = maxi
    p = P
    while i >= 0:
        wanted = T[i]
        for j in range(n):
            if copy[j] == wanted:
                ans.append(j)
                break

        if p < 0:
            break

        tmp = T[i]
        diff = F[i][p] - ((b(T, i) - a(T, i)) * h(T, i))
        p -= T[i][3]
        # i -= 1

        if diff == 0:
            break

        while i >= 0 and p >= 0:
            if tmp[1] <= a(T, i):
                i -= 1
                continue
            if F[i][p] == diff:
                break
            i -= 1

    # print(maxval)

    return ans


runtests( select_buildings, all_tests=True )