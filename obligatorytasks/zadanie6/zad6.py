from zad6testy import runtests
from collections import deque


def longer(G, s, t):

    n = len(G)
    Q = deque()
    visited = [False for _ in range(n)]
    distances = [0] * n
    parents = [None for _ in range(n)]

    distances[s] = 0
    visited[s] = True
    Q.append(s)
    flag = False

    bridge = 0

    while Q:

        if len(Q) == 1:
            bridge += 1
        else:
            bridge = 0

        if bridge == 2:
            x = Q.popleft()
            y = parents[x]
            return x, y

        u = Q.popleft()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distances[v] = distances[u] + 1
                parents[v] = u
                Q.append(v)

                if v == t:
                    flag = True
                    break

        if flag:
            break

    if distances[t] == 0:
        return None

    d = distances[t]
    path = [t]
    i = t
    while parents[i] is not None:
        path.append(parents[i])
        i = parents[i]

# -----------------------------------------------------------------

    i, j = 0, 1
    while j < len(path):
        v1 = path[i]
        v2 = path[j]

        Q = deque()
        visited = [False for _ in range(n)]
        distances = [0] * n
        flag = False

        distances[s] = 0
        visited[s] = True
        Q.append(s)

        while Q:

            u = Q.popleft()

            for v in G[u]:
                if (u == v1 and v == v2) or (v == v1 and u == v2):
                    continue
                if not visited[v]:
                    visited[v] = True
                    distances[v] = distances[u] + 1
                    Q.append(v)

                    if v == t:
                        flag = True
                        break

            if flag:
                break

        i, j = j, j + 1

        if distances[t] > d:
            return v2, v1

    # print(path)
    # print(d)
    # print(parents)
    # print(distances)

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
