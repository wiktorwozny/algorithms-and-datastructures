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


def kruskal(G):

    n = len(G)
    result = []
    nodes = []

    liczba = 0

    for i in range(n):
        liczba = max(liczba, G[i][0])
        liczba = max(liczba, G[i][1])

    for i in range(liczba + 1):
        nodes.append(Node(i))

    G.sort(key=lambda item: item[2])

    e = i = 0

    while e < liczba and i < len(G):

        u, v, w = G[i]
        i += 1
        x = find(nodes[u])
        y = find(nodes[v])

        if x != y:
            e += 1
            result.append([u, v, w])
            union(nodes[u], nodes[v])

    if e < liczba:
        return None

    return result


graph = [[0, 1, 1], [0, 2, 6], [1, 4, 2], [1, 7, 10], [2, 3, 5], [3, 4, 3], [3, 5, 8], [4, 6, 4], [5, 6, 7], [6, 7, 9], [7, 8, 11]]

print(kruskal(graph))

