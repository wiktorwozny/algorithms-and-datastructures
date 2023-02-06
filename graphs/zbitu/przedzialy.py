from collections import deque


def czymozna(tab, partition):

    a, b = partition[0], partition[1]
    n = b - a + 1

    graph = [[0] * n for _ in range(n)]

    for x in tab:
        if x[0] < a or x[1] > b:
            continue
        graph[x[0] - a][x[1] - a] = 1

    visited = [False] * n
    queue = deque()
    queue.append(0)
    visited[0] = True

    while queue:
        u = queue.popleft()

        if u == b - a:
            return True

        for v in range(n):
            if not visited[v] and graph[u][v]:
                queue.append(v)
                visited[v] = True

    return False


przedzialy = [[0, 2], [1, 3], [2, 4], [0, 3], [3, 5], [5, 6], [3, 4]]
print(czymozna(przedzialy, [1, 4]))

