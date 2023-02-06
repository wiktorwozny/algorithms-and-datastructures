from kol2atesty import runtests
from math import inf


def rec(tab, idx, osoba, DP):

    if idx == 0 and osoba == 1:
        return inf

    if idx == 0 and osoba == 0:
        return 0

    if idx < 0:
        return inf

    if DP[idx][osoba] is not None:
        return DP[idx][osoba]

    mini = inf
    if osoba == 0:  # mietek
        for i in range(idx - 3, idx):
            if i >= 0:
                if rec(tab, i, 1, DP) + tab[idx] - tab[i] < mini:
                    mini = rec(tab, i, 1, DP) + tab[idx] - tab[i]

    else:  # jacek
        for i in range(idx - 3, idx):
            if i >= 0:
                if rec(tab, i, 0, DP) < mini:
                    mini = rec(tab, i, 0, DP)

    DP[idx][osoba] = mini
    return mini


def drivers(P, B):

    # mietek = 0, jacek = 1

    n = len(P)
    copy = []
    for i in range(n):
        copy.append(P[i])

    P.sort(key=lambda x: x[0])

    tab = [0]
    control = 0
    for i in range(n):
        if not P[i][1]:
            control += 1
        else:
            tab.append(control)

    tab.append(control)

    DP = [[None for _ in range(2)] for _ in range(len(tab))]

    w1 = rec(tab, len(tab) - 1, 0, DP)

    DP = [[None for _ in range(2)] for _ in range(len(tab))]
    w2 = rec(tab, len(tab) - 1, 1, DP)

    print(min(w1, w2))

    ans = []
    i = len(tab) - 1
    if w1 > w2:
        osoba = 0
    else:
        osoba = 1

    while i > 0:
        mini = inf
        best = -1
        if osoba == 1:
            for j in range(i - 3, i):
                if rec(tab, j, 0, DP) < mini:
                    mini = rec(tab, i, 0, DP)
                    best = j
            osoba = 0
        else:
            for j in range(i - 3, i):
                if rec(tab, j, 1, DP) + tab[i] - tab[j] < mini:
                    mini = rec(tab, j, 1, DP) + tab[i] - tab[j]
                    best = j

        i = best
        ans.append(best)

    print(tab)
    print(ans)

    return []


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(drivers, all_tests=True)
