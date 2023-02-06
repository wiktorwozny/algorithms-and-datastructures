from zad8testy import runtests
from math import ceil, sqrt


class Node:
    def __init__(self, value):  # value moze przechowywac na przyklad numer wierzcholka
        self.parent = self
        self.value = value
        self.rank = 0   # rank to oszacowanie na rozmiar zbioru (wysokosc), zeby opreacja union szybko dzialala


def find(x):  # jednoczesnie bedziemy kompresowac sciezke tak zeby drzewo bylo jak najmniejsze

    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent


def union(x, y):  # zbior o mniejszej randze dolaczamy do tego o wiekszej randze

    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(G, liczba):

    # print(G)
    # input()

    result = []
    nodes = []

    # for i in range(n):
    #     liczba = max(liczba, G[i][0])
    #     liczba = max(liczba, G[i][1])

    for i in range(liczba + 1):
        nodes.append(Node(i))

    # G.sort(key=lambda item: item[2])

    for i in range(len(G)):

        if len(result) == liczba:
            break

        u, v, w = G[i]
        x = find(nodes[u])
        y = find(nodes[v])

        if x != y:
            result.append([u, v, w])
            union(nodes[u], nodes[v])

    return result


def d(i, j, A):

    x = ceil(sqrt((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2))

    return x


def highway(A):

    n = len(A)
    graph = []

    for i in range(n):
        for j in range(i + 1, n):
            graph.append([i, j, d(i, j, A)])

    graph.sort(key=lambda item: item[2])

    result = kruskal(graph, n - 1)
    ans = result[-1][2] - result[0][2]

    while len(graph) >= n:

        graph.pop(0)

        result = kruskal(graph, n - 1)
        # print("asdasdasd", result)

        if len(result) != len(A) - 1:
            break

        ans = min(ans, result[-1][2] - result[0][2])

    return ans


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(highway, all_tests=True)
