from kol2atesty import runtests
from math import inf


def rec(P, idx, kto, ile, DP):

    if idx == len(P):
        return 0

    if DP[idx][ile][kto] is not None:
        return DP[idx][ile][kto]

    if P[idx][1]:  # punkt przesiadkowy
        if ile == 0:  # wymuszamy przesiadke
            w1 = rec(P, idx + 1, (kto + 1) % 2, 2, DP)
            DP[idx][ile][kto] = w1
            return DP[idx][ile][kto]

        else:
            w1 = rec(P, idx + 1, (kto + 1) % 2, 2, DP)  # zmieniaja sie choc nie musza
            w2 = rec(P, idx + 1, kto, ile - 1, DP)  # bez zmiany
            DP[idx][ile][kto] = min(w1, w2)
            return DP[idx][ile][kto]

    else:
        w1 = rec(P, idx + 1, kto, ile, DP) + kto
        DP[idx][ile][kto] = w1
        return DP[idx][ile][kto]


def drivers(P, B):

    n = len(P)
    copy = [[0 for _ in range(3)] for _ in range(n)]

    for i in range(n):
        copy[i][0], copy[i][1], copy[i][2] = P[i][0], P[i][1], i

    copy.sort()

    DP = [[[None for _ in range(2)] for _ in range(3)] for _ in range(n)]

    x = rec(copy, 0, 0, 2, DP)

    tab = []
    idx = 0
    kto = 0
    ile = 2

    while idx < len(P):
        if copy[idx][1]:
            if ile == 0:
                tab.append(copy[idx][2])
                kto = (kto + 1) % 2
                ile = 2
            else:
                w1 = rec(P, idx + 1, (kto + 1) % 2, 2, DP)
                w2 = rec(P, idx + 1, kto, ile - 1, DP)
                if w1 > w2:
                    ile -= 1
                else:
                    kto = (kto + 1) % 2
                    ile = 2
                    tab.append(copy[idx][2])

        idx += 1

    # print(tab)

    return tab


runtests(drivers, all_tests=True)




