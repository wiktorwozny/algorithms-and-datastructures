from egz1atesty import runtests


# algorytm dynamiczny z funkcją f(i, j, d) gdzie i to jest indeks do którego już wcześniej dojechaliśmy z zachodu
# j to indeks do którego już wcześniej dojechaliśmy ze wschodu, a d to ile dni już minęło od początku zbierania
# f(i, j, d) = max (po i < k < j) (f(k + 1, j, d + 1) + S[k] - d, f(i, k - 1, d + 1) + S[k] - d)
# złożoność algorytmu zgaduję że n ^ 4 bo sie nie robia testy


def f(S, i, j, d, DP):

    if i >= j:
        return 0

    if d >= len(S):
        return 0

    if DP[i][j][d] is not None:
        return DP[i][j][d]

    maxik = -1
    for k in range(i, j + 1):
        zachod = f(S, k + 1, j, d + 1, DP) + S[k] - d
        wschod = f(S, i, k - 1, d + 1, DP) + S[k] - d
        maxik = max(maxik, zachod, wschod)

    DP[i][j][d] = maxik
    return maxik


def snow(S):

    n = len(S)

    DP = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]

    x = f(S, 0, n - 1, 0, DP)

    return x


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=False)
