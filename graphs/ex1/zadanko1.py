from queue import PriorityQueue as PQ
from math import inf
from zad3testy import runtests


def relax(w, parents, u, v, distance):

    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parents[v] = u


def djikstra(G, s):

    n = len(G)
    visited = [False] * n
    parents = [None] * n
    distance = [inf] * n
    queue = PQ()

    queue.put((0, s))
    visited[s] = True
    distance[s] = 0

    while not queue.empty():
        d, u = queue.get()

        for v, w in G[u]:
            if not visited[v]:
                relax(w, parents, u, v, distance)
                queue.put((distance[v], v))

        visited[u] = True

    return distance


def paths(G, s, t):

    n = len(G)

    sdistances = djikstra(G, s)
    tdistances = djikstra(G, t)

    path = sdistances[t]
    if path is inf:
        return 0
    used = []

    for u in range(n):
        for v, w in G[u]:
            if sorted([u, v]) not in used:
                if sdistances[u] + w + tdistances[v] == path or sdistances[v] + w + tdistances[u] == path:
                    used.append(sorted([u, v]))

    return len(used)


G = [
    [(1,2),(2,4)],
    [(0,2),(3,11),(4,3)],
    [(0,4),(3,13)],
    [(1,11),(2,13),(5,17),(6,1)],
    [(1,3),(5,5)],
    [(3,17),(4,5),(7,7)],
    [(3,1),(7,3)],
    [(5,7),(6,3)]
    ]

runtests(paths)
