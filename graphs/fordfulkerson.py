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
            if v != u and not visited[v] and G[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parents[v] = u
                if v == t:
                    return True

    return False


def fulkerson(G, source, sink):

    n = len(G)
    parents = [None for _ in range(n)]
    flow = 0

    while True:

        if not bfs(G, source, sink, parents):
            break

        path = 10**10
        s = sink
        while s != source:
            path = min(path, G[parents[s]][s])
            s = parents[s]

        flow += path

        v = sink
        while v != source:
            G[parents[v]][v] -= path
            G[v][parents[v]] += path
            v = parents[v]

    return flow


graph = [[0, 4, 2, 0, 0, 0],
         [0, 0, 2, 2, 0, 0],
         [0, 0, 0, 2, 2, 0],
         [0, 0, 0, 0, 0, 4],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0]]

print(fulkerson(graph, 0, len(graph) - 1))
