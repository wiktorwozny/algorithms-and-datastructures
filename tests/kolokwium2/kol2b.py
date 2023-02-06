# Wiktor Woźny 410434
# na początku sortuję tablicę O po odległościach, odpowiednio zmieniam tablicę cen C, żeby indeksy zgadzały się z tablicą
# odległości, następnie wykonuję algorytm dynamiczny, rozpatruję trzy przypadki, pierwszy to jak możemy jechać dalej to
# jedziemy dalaj, drugi bierze pod uwagę, że możemy jeszcze skorzystać z warunku podanego w punkcie drugim, jak nie można
# to jedziemy zmieniając zmienną we funkcji, a trzeci bierze pod uwagę, że robimy postój na parkingu, szkoda że nie działa :(

from kol2btesty import runtests
from math import inf


# def f(O, C, T, i, ilemozna, czymozna, DP, L):
#
#     if ilemozna > 2 * T:
#         ilemozna = T
#
#     if i == len(O) - 1:
#         if ilemozna - (L - O[i]) >= 0:  # jeżeli z ostatniej stacji dojedziemy to jedziemy
#             return 0
#         elif ilemozna + T - (L - O[i]) >= 0 and czymozna:
#             return 0
#         else:
#             return C[i]  # jeżeli się nie da to musimy wziąć postój
#
#     if DP[i][czymozna] is not None:
#         return DP[i][czymozna]
#
#     odleglosc = O[i + 1] - O[i]  # odleglosc do przejechania (do nastepnej stacji)
#
#     w1 = 10**100
#     w2 = 10**100
#
#     if ilemozna - odleglosc >= 0:
#         w1 = f(O, C, T, i + 1, ilemozna - odleglosc, czymozna, DP, L)  # jedziemy dalej
#
#     if ilemozna - odleglosc < 0 and ilemozna + T - odleglosc >= 0 and czymozna:
#         w2 = f(O, C, T, i + 1, ilemozna + T - odleglosc, 0, DP, L)
#         # z warunku
#
#     w3 = f(O, C, T, i + 1, T - odleglosc, czymozna, DP, L) + C[i]  # robimy postój
#
#     DP[i][czymozna] = min(w1, w2, w3)
#
#     return DP[i][czymozna]
#
#
# def min_cost( O, C, T, L ):
#
#     n = len(O)
#     DP = [[None for _ in range(2)] for _ in range(n)]
#
#     sortowana = [[0, 0] for _ in range(n)]
#
#     for i in range(n):
#         sortowana[i][0] = O[i]
#         sortowana[i][1] = i
#
#     sortowana.sort(key=lambda tup: tup[0])
#     newO = [0] * n
#     newC = [0] * n
#
#     for i in range(n):
#         newO[i] = O[sortowana[i][1]]
#         newC[i] = C[sortowana[i][1]]
#
#     x = f(newO, newC, T, 0, T - newO[0], 1, DP, L)
#
#     return x


def rec(O, C, T, L, idx, warunek, DP):

    if O[idx] >= L:
        DP[warunek][idx] = 0
        return 0

    if O[idx] + T >= L or (warunek == 1 and O[idx] + 2 * T >= L):
        DP[warunek][idx] = C[idx]
        return C[idx]

    if DP[warunek][idx] != -1:
        return DP[warunek][idx]

    mini = 10**10
    for i in range(idx + 1, len(O)):
        if O[i] - O[idx] <= T:
            mini = min(rec(O, C, T, L, i, warunek, DP), mini)
        elif O[i] - O[idx] <= 2 * T and warunek == 1:
            mini = min(rec(O, C, T, L, i, 0, DP), mini)
        else:
            break

    DP[warunek][idx] = mini + C[idx]
    return mini + C[idx]


def min_cost(O, C, T, L):

    n = len(O)
    DP = [[-1 for _ in range(n)] for _ in range(2)]

    sortowana = [[0, 0] for _ in range(n)]

    for i in range(n):
        sortowana[i][0] = O[i]
        sortowana[i][1] = i

    sortowana.sort(key=lambda tup: tup[0])
    newO = [0] * n
    newC = [0] * n

    for i in range(n):
        newO[i] = O[sortowana[i][1]]
        newC[i] = C[sortowana[i][1]]

    mini = 10**10
    for i in range(len(O)):
        if newO[i] <= T:
            mini = min(rec(newO, newC, T, L, i, 1, DP), mini)
        elif newO[i] <= 2 * T:
            mini = min(rec(newO, newC, T, L, i, 0, DP), mini)
        else:
            break


    # print(newO)
    # print(newC)
    # input()

    return mini


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
