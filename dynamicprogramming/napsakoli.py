def knapsack(W, P, B):  # W - zbiór wag, P - zbiór cen, B - wartość

    n = len(W)
    F = [[0 for b in range(B + 1)] for i in range(n)]  # drugi indeks to wagi b, pierwszy to nasze i (patrz opis zadania)

    for b in range(W[0], B + 1):  # warunki brzegowe
        F[0][b] = P[0]

    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])

    odp = []  # odtwarzanie rozwiązania
    i = n - 1
    b = B
    while i > 0:
        if F[i][b] != F[i - 1][b]:
            odp.append(i)
            b = b - W[i]
        i -= 1

    if b >= W[i]:
        odp.append(i)

    print(odp[::-1])

    return F[n - 1][B]


tab_w = [10,   40,  10,  15,  12,  30,  5]
tab_p = [60,  100,  120, 80,  30,  50,  100]
cap = 50


def rek(W, P, B, idx, DP):

    if idx == len(W) - 1:
        if B - W[idx] >= 0:
            DP[idx][B] = P[idx]
            return P[idx]
        else:
            DP[idx][B] = 0
            return 0

    if DP[idx][B] is not None:
        return DP[idx][B]

    maksiu = -1
    for i in range(idx + 1, len(W)):
        if B - W[i] >= 0:
            maksiu = max(maksiu, rek(W, P, B - W[idx], i, DP))

    DP[idx][B] = maksiu + P[idx]
    return maksiu + P[idx]


def napsakens(W, P, B):

    n = len(W)
    DP = [[None for _ in range(B + 1)] for _ in range(n)]

    maksiu = -1
    for i in range(n):
        if B - W[i] >= 0:
            maksiu = max(maksiu, rek(W, P, B, i, DP))

    return maksiu


print(napsakens(tab_w, tab_p, cap))
