from zad3testy import runtests


def insertion_sort(T):  # O(n^2), very little memory needed
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


def SortTab(T, P):

    # return sorted(T)

    minstart = float("inf")
    maxstart = -1
    for i in range(len(P)):
        minstart = min(minstart, P[i][0])
        maxstart = max(maxstart, P[i][0])

    diff = maxstart - minstart + 1
    counts = [0] * diff
    output = [0] * len(P)

    for x in P:
        counts[x[0] - minstart] += 1

    for i in range(1, diff):
        counts[i] += counts[i - 1]

    for i in range(len(P) - 1, -1, -1):
        output[counts[P[i][0] - minstart] - 1] = P[i]
        counts[P[i][0] - minstart] -= 1

    for i in range(len(P)):
        P[i] = output[i]

    i = 0
    buckets = 0
    while i < len(P):
        b = P[i][1]
        j = i
        n = 0
        while j < len(P) and b >= P[j][0]:
            b = max(b, P[j][1])
            n += P[j][2]
            j += 1
        i = j

        buckets += int(n * len(T))

    B = [[] for _ in range(buckets + 1)]
    a = min(T)
    b = max(T)

    for i in range(len(T)):
        index = int(((T[i] - a) / (b - a)) * buckets)
        B[index].append(T[i])

    tmp = 0
    for i in range(buckets + 1):
        for j in range(len(B[i])):
            T[tmp] = B[i][j]
            tmp += 1

    insertion_sort(T)

    print(buckets)
    return T

    # minimum = float('inf')
    # maximum = -1
    #
    # for i in range(len(P)):
    #     minimum = min(minimum, P[i][0])
    #     maximum = max(maximum, P[i][1])
    #
    # n = maximum - minimum
    # buckets = [[] for _ in range(n)]




runtests(SortTab)
