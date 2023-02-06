from egz1btesty import runtests


# Wiktor Woźny, 410434, sprawdzam który poziom w drzewie jest najlepszy, wybieram go i potem nieudolnie liczę ile
# krawędzi należy usunąć


class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow


def countlevels(T, l, levels):

    T.x = l
    levels[l] += 1

    if T.left is not None:
        countlevels(T.left, l + 1, levels)
    if T.right is not None:
        countlevels(T.right, l + 1, levels)


def count(T, n):

    n[0] += 1
    if T.left is not None:
        count(T.left, n)
    if T.right is not None:
        count(T.right, n)


def solve(T, bestlevel, x):

    if T.left is None and T.right is None and T.x < bestlevel:
        x[0] += 1  # najprawdopodobniej tu sie zle zlicza ale nie mam innego pomyslu jak to lepiej zrobic sadge
        return

    if T.left is None and T.right is None and T.x == bestlevel:
        return

    if T.x > bestlevel:
        x[0] += 1
        return

    if T.left is not None:
        solve(T.left, bestlevel, x)

    if T.right is not None:
        solve(T.right, bestlevel, x)


def wideentall(T):

    n = [0]
    count(T, n)
    size = n[0]
    levels = [0 for _ in range(size)]

    root = T
    temp = root

    countlevels(temp, 0, levels)

    besti = -1
    maxik = -1
    for i, nodes in enumerate(levels):
        if nodes >= maxik:
            maxik = nodes
            besti = i

    x = [0]
    solve(root, besti, x)

    return x[0]


runtests(wideentall, all_tests=False)
