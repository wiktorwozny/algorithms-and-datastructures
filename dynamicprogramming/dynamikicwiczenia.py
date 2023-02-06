def lis(A):  # longest increasing subsequence
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    return max(F), F, P


def print_sol(A, P, i):
    if P[i] != -1:
        print_sol(A, P, P[i])

    print(A[i])


# problem imprezy firmowej, mamy dane drzewo, które opisuje strukture firmy, jest szef wszystkich szefów, potem niżej
# każdy ma jakiś podpracowników, szefów, dla każdego jest przypisany współczynnik śmieszności, ważne jest, że nie
# możemy wziąć bezpośrednich szefów ludzi, których bierzemy na imprezę, chcemy uzyskać jak największą sumę
# współczynników śmieszności

# f(v) - wartość najlepszej imprezy poddrzewa zakorzenionego w v
# g(v) - jak wyżej, pod warunkiem, że v nie idzie na imprezę

# wynik - f(root)

class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []  # tablica dzieci węzła
        self.f = -1
        self.g = -1


def g(v):

    if v.g != -1:
        return v.g

    v.g = 0
    for u in v.emp:
        v.q += f(u)

    return v.g


def f(v):

    if v.f != -1:
        return v.f

    f1 = g(v)
    f2 = v.fun

    for u in v.emp:
        f2 += g(u)

    v.f = max(f1, f2)

    return v.f


# problem plecakowy, mamy zbiór przedmiotów ( I = [0 .. n - 1] ) każdy przedmiot ma przypisaną jakąś wagę w oraz
# każdy przedmiot ma przypisany jakiś profit/cenę p, dodatkowo mamy daną pojemność B. Zadanie: znaleźć podzbiór I o
# maksymalnej sumarycznej cenie(profitu) i łącznej wadze nie przekraczającej B

# f(i, b) - maksymalna suma cen przedmiotów ze zbioru [0 .. i] nie przekraczających łącznej wagi b

# wynik: f(n, B)

# sformułowanie rekurencyjne: f(i, b) = max( f(i - 1, b), f(i - 1, b - w(i)) + p(i) )

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


# tab_w = [10,   40,  10,  15,  12,  30,  5]
# tab_p = [60,  100,  120, 80,  30,  50,  100]
# cap = 50
# print(knapsack(tab_w, tab_p, cap))


# mamy daną tablicę A[1 .. n], chcemy znaleźć, czy istnieje taka suma elementów z niej dająca sumę T. (zakładamy, że
# wszystkie elementy w tablicy A są mniejsze od T)

# f(i, t) True/False czy w podtablicy A[0 .. i] da się osiągnąć sumę t <= T

def select_sum(A, T):
    n = len(A)

    F = [[False for t in range(T + 1)] for i in range(n)]

    F[0][A[0]] = True

    for i in range(n):
        F[i][0] = True

    for i in range(1, n):
        for t in range(T + 1):
            F[i][t] = F[i - 1][t]
            if t - A[i] >= 0 and F[i - 1][t - A[i]]:
                F[i][t] = True

    # for x in F:
    #     print(x)

    return F[n - 1][T]


# print(select_sum([2, 1, 10, 5], 15))


# mamy dane dwie tablice A, B, każda o rozmiarze n. Chcemy znaleźć najdłuższy wspólny podciąg

# f(i, j) - długość najdłuższego wspólnego podciągu w tablicach A[0 .. i] i B[0 .. j]

def lcs(A, B):

    n = len(A)

    F = [[0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i][j - 1], F[i - 1][j])

    return F[n][n]


# problem wycinania drzew, wycinamy drzewa na kolejnych indeksach, problem jest taki, że nie możemy wyciąć dwóch drzew
# na kolejnych indeksach

def forest(T):

    n = len(T)
    W = [0] * n

    W[0] = T[0]
    W[1] = max(T[0], T[1])

    for i in range(2, n):
        W[i] = max(W[i - 1], W[i - 2] + T[i])

    return W


# tab = [5, 2, 7, 5, 7, 8, 5, 7, 5]
# print(forest(tab))

# mamy daną tablicę zawierającą przedziały, które zajmują klocki, klocki spadają na oś liczbową, chcemy uzyskać jak
# najwyższą wieżą usuwając klocki, które nie pasują (wystają), zwracamy jej wysokość

# f(i) = max(f(j)) + 1
#          0 <= j < i:
#       A[j][0] <= A[i][0]
#       A[j][1] >= A[i][1]


def kloc(A, i, DP):

    if DP[i] is not None:
        return DP[i]

    maxval = 0
    for j in range(i):
        if A[j][0] <= A[i][0] and A[j][1] >= A[i][1]:
            maxval = max(maxval, kloc(A, j, DP))

    DP[i] = maxval + 1
    return DP[i]


def klocAux(A):

    DP = [None for i in range(len(A))]

    maxval = 0
    for i in range(len(A)):
        maxval = max(maxval, kloc(A, i, DP))

    return maxval


# A = [[1, 6], [2, 4], [3, 5], [3, 4], [1, 6]]
# print(klocAux(A))


# dostajemy tablicę (M x N) wypełnioną wartościami. Mamy za zadanie znaleźć najdłuższą ścieżkę w tej tablicy (możemy
# przechodzić na pola sąsiadujące krawędziami), o rosnących wartościach (to znaczy, że z pola o wartości 3, mogę przejść
# na pola o wartości większej bądź równej 4).


# NIE DZIALA

def rec(T, x, y, DP):

    M = len(T)
    N = len(T[0])

    if DP[x][y] is not None:
        return DP[x][y]

    if x - 1 >= 0 and T[x - 1][y] < T[x][y]:
        return rec(T, x - 1, y, DP) + 1
    if y - 1 >= 0 and T[x][y - 1] < T[x][y]:
        return rec(T, x, y - 1, DP) + 1
    if x + 1 < M and T[x + 1][y] < T[x][y]:
        return rec(T, x + 1, y, DP) + 1
    if y + 1 < N and T[x][y + 1] < T[x][y]:
        return rec(T, x, y + 1, DP) + 1

    return 1


def path(T, x, y):

    M = len(T)
    N = len(T[0])

    DP = [[None for y in range(N)] for x in range(M)]

    DP[x][y] = 1

    max_val = -1

    for i in range(M):
        for y in range(N):
            max_val = max(max_val, rec(T, i, y, DP))

    for i in range(M):
        print(DP[i])

    return max_val


# tab = [[0, 2, 7, 10],
#        [7, 4, 3, 9],
#        [2, 5, 8, 9]]
#
# print(path(tab, 0, 0))


# zaba z okreslona maksymalna pojemnoscia baku q, mamy przebyc l, stacje sa odlegle od punktu startu o T[i], na stacji
# mozna wlac V[i] paliwa, dynamik


def recursion(i, m, T, V, q, l, DP):

    if m > q:
        return 10**100

    if i <= 0:
        return 1

    if DP[i][m] is not None:
        return DP[i][m]

    w1 = recursion(i - 1, m + (T[i] - T[i - 1]), T, V, q, l, DP)
    w2 = recursion(i - 1, max(m - V[i], 0) + (T[i] - T[i - 1]), T, V, q, l, DP) + 1

    DP[i][m] = min(w1, w2)
    return DP[i][m]


def iamlate(T, V, q, l):

    n = len(T)

    DP = [[None for i in range(l + 1)] for j in range(n)]

    x = l - T[n - 1]

    ilosc = recursion(n - 1, x, T, V, q, l, DP)

    # for i in range(n):
    #     print(DP[i])

    sol = []
    i = n - 1
    m = x
    while i >= 0:
        w1 = recursion(i - 1, m + (T[i] - T[i - 1]), T, V, q, l, DP)
        w2 = recursion(i - 1, max(m - V[i], 0) + (T[i] - T[i - 1]), T, V, q, l, DP) + 1

        if w1 > w2:
            i -= 1
            m = max(m - V[i], 0) + (T[i] - T[i - 1])
            sol.append(i)
        else:
            i -= 1
            m += (T[i] - T[i - 1])

    return sol


T = [0, 1, 2]
V = [2, 1, 5]
q = 2
l = 4

print(iamlate(T, V, q, l))


