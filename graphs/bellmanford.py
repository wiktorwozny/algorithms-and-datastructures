def relax(u, v, w, parents, distance):

    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parents[v] = u


def bellman(G):  # wbija postac krawedziowa

    n = len(G)

    liczba = 0

    for i in range(n):
        liczba = max(liczba, G[i][0])
        liczba = max(liczba, G[i][1])

    distance = [float("inf") for _ in range(liczba + 1)]
    parents = [None for _ in range(liczba + 1)]

    distance[0] = 0

    for i in range(liczba):
        for edge in G:
            u, v, w = edge
            relax(u, v, w, parents, distance)

    # weryfikacja czy mamy ujemny cykl:
    for edge in G:
        u, v, w = edge
        if distance[v] > distance[u] + w:
            return "cykl jest ujemny"

    return distance


graph = [[0,1,1],[0,7,2],[1,0,1],[1,2,2],[1,4,3],[2,1,2],[2,3,5],[3,2,5],[3,6,1],[4,1,3],[4,5,3],[4,7,1],[5,4,3],
        [5,6,8],[5,8,1],[6,3,1],[6,5,8],[6,8,4],[7,0,2],[7,4,1],[7,8,7],[8,5,1],[8,6,4],[8,7,7]]

print(bellman(graph))
