from queue import PriorityQueue as PQ
from math import inf


# def prim(G):
#
#     n = len(G)
#     queue = PQ()
#     visited = [False] * n
#     parents = [None] * n
#     put = [False] * n
#     state = [None] * n
#
#     queue.put([0, 0])
#     put[0] = True
#
#     while not queue.empty():
#         x = queue.get()
#
#         if not visited[x[1]]:
#
#             for u in G[x[1]]:
#                 if not put[u[0]]:
#                     queue.put([u[1], u[0]])
#                     put[u[0]] = True
#                     parents[u[0]] = x[1]
#                     state[u[0]] = u[1]
#                 else:
#                     if not visited[u[0]]:
#                         queue.put([u[1], u[0]])
#                         if state[u[0]] > u[1]:
#                             parents[u[0]] = x[1]
#                             state[u[0]] = u[1]
#
#         visited[x[1]] = True
#
#     ans = []
#     for i in range(1, n):
#         ans.append(sorted([i, parents[i]]))
#
#     return ans


def prim(G):

    n = len(G)
    visited = [False] * n
    parents = [None] * n
    state = [inf] * n
    queue = PQ()

    queue.put((0, 0))
    visited[0] = True
    state[0] = 0

    while not queue.empty():
        d, u = queue.get()

        for v, w in G[u]:
            if not visited[v]:
                if state[v] >= w:
                    state[v] = w
                    parents[v] = u
                    queue.put((w, v))

        visited[u] = True

    ans = []
    for i in range(1, n):
        ans.append(sorted([i, parents[i]]))

    return ans


graph = [[(1, 1), (2, 3)], [(0, 1), (3, 2), (4, 4)], [(0, 3), (3, 1), (4, 2)], [(1, 2), (2, 1), (5, 1)],
         [(1, 4), (2, 2), (5, 3)], [(3, 1), (4, 3)]]


print(prim(graph))
