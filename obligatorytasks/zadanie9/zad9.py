from zad9testy import runtests
from collections import deque


def bfs(G, s, t, parents):

    n = len(G)
    visited = [False] * n
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.popleft()

        for v in range(len(G[u])):
            if not visited[v] and G[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parents[v] = u
                if v == t:
                    path = []
                    while v != s:
                        path.append([parents[v], v])
                        v = parents[v]
                    return path

    return None


def fulkerson(G, s, t):

    n = len(G)
    parents = [None for _ in range(n)]
    flow = 0

    while True:

        path = bfs(G, s, t, parents)

        if path is None:
            break

        current = 10**10

        for x, y in path:
            current = min(current, G[x][y])

        flow += current

        for x, y in path:
            G[x][y] -= current
            G[y][x] += current

    return flow


def maxflow(G, s):

    n = len(G)
    num = -1

    for i in range(n):
        num = max(num, G[i][0])
        num = max(num, G[i][1])

    num += 1
    ans = 0

    M = [[0 for _ in range(num + 1)] for _ in range(num + 1)]

    for u, v, w in G:
        M[u][v] = w

    for t1 in range(num):
        for t2 in range(t1 + 1, num):
            if t1 == s or t2 == s:
                continue

            M[t1][num] = 10**7
            M[t2][num] = 10**7

            flow = fulkerson(M, s, num)

            ans = max(ans, flow)

            M = [[0 for _ in range(num + 1)] for _ in range(num + 1)]
            for u, v, w in G:
                M[u][v] = w

    return ans


runtests(maxflow, all_tests=True)
