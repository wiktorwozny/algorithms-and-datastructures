from zad2testy import runtests


def dfs(G, s):

    n = len(G)
    visited = [False] * n
    parents = [None] * n
    dfsvisit(G, s, visited, parents)

    return parents


def dfsvisit(G, u, visited, parents):

    visited[u] = True
    for v in range(len(G)):
        if G[u][v] != 0 and not visited[v]:
            parents[v] = u
            dfsvisit(G, v, visited, parents)


def breaking(G):

    n = len(G)
    maksik = -1
    ans = None

    for i in range(n):
        parents = dfs(G, i)
        counter = 0

        for j in range(n):
            if parents[j] == i:
                counter += 1

        if counter == 1:
            continue

        if counter > maksik:
            maksik = counter
            ans = i

    return ans


runtests(breaking)
