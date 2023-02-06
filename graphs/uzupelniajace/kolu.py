from kolutesty import runtests
from collections import deque


def discs(graph, disk, prevs, start):

    n = len(disk)
    stacks = [deque() for _ in range(2)]
    for i in range(n):
        if prevs[i] == 0 and disk[i] == 'A':
            stacks[0].append(i)
        if prevs[i] == 0 and disk[i] == 'B':
            stacks[1].append(i)

    nr = start
    ans = 0
    while stacks[0] or stacks[1]:
        while stacks[nr]:
            u = stacks[nr].pop()

            for v in graph[u]:
                prevs[v] -= 1
                if prevs[v] == 0 and disk[v] == 'A':
                    stacks[0].append(v)
                if prevs[v] == 0 and disk[v] == 'B':
                    stacks[1].append(v)

        nr = (nr + 1) % 2
        ans += 1

    for x in prevs:
        if x != 0:
            return -1

    return ans - 1


def swaps(disk, depends):

    n = len(disk)
    graph = [[] for _ in range(n)]
    prevs = [0] * n

    for i in range(n):
        prevs[i] = len(depends[i])

        for u in depends[i]:
            graph[u].append(i)

    c1 = discs(graph, disk, prevs, 0)
    c2 = discs(graph, disk, prevs, 1)

    if c1 == -1:
        return c2
    if c2 == -1:
        return c1

    return min(c1, c2)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(swaps, all_tests = True)

