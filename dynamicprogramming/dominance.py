def dominance(P):

    n = len(P)
    S = []
    copy = []
    for i, x in enumerate(P):
        copy.append((x[0], x[1], i))

    copy.sort(key=lambda t: t[1])
    copy.sort(key=lambda t: t[0])

    S.append(copy[0][2])

    for i in range(1, n):
        for x in S:
            if P[x][0] <= copy[i][0] and P[x][1] <= copy[i][1]:
                break
        else:
            S.append(copy[i][2])

    return S


P = [(2, 2), (1, 1), (2.5, 0.5), (3, 2), (0.5, 3)]
print(dominance(P))
