from queue import PriorityQueue as PQ
from math import inf


def relax(w, parents, u, v, distance):

    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parents[v] = u


# def djikstra(G):
#
#     n = len(G)
#     parents = [None] * n
#     visited = [False] * n
#     distance = [0] * n
#     put = [False] * n
#
#     queue = PQ()
#     queue.put([0, 0])
#     put[0] = True
#
#     while not queue.empty():
#         x, u = queue.get()
#
#         if not visited[u]:
#             for v in G[u]:
#                 if not put[v[0]]:
#                     d = distance[u] + v[1]
#                     queue.put([d, v[0]])
#                     parents[v[0]] = u
#                     put[v[0]] = True
#                     distance[v[0]] = d
#                 else:
#                     if not visited[v[0]]:
#                         w = v[1]
#                         relax(w, parents, u, v[0], distance)
#                         queue.put([distance[v[0]], v[0]])
#
#         visited[u] = True
#
#     a = 8
#     path = []
#     while a is not None:
#         path.append(a)
#         a = parents[a]
#
#     # print(parents)
#     print(sorted(path))
#
#     return distance

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

    return distance, parents


# graph = [ [(1,1),(7,2)], [(0,1),(2,2),(4,3)], [(1,2),(3,5)], [(2,5),(6,1)], [(1,3),(5,3),(7,1)], [(4,3),(6,8),(8,1)], [(3,1),(5,8),(8,4)],
#          [(0,2),(4,1),(8,7)],[(5,1),(6,4),(7,7)]]

graph = [
    [(1, 1)],
    [(0, 1), (2, 2), (3, 3)],
    [(1, 2), (3, 1), (4, 5)],
    [(1, 3), (2, 1), (4, 1)],
    [(2, 5), (3, 1)]
]


print(djikstra(graph, 1))
