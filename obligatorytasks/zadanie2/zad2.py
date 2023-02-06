from zad2testy import runtests
from random import randint


def quickSort(ar):

    if len(ar) <= 1:
        return ar

    else:
        mid = len(ar) // 2
        pivot = ar[mid]

        smaller, greater = [], []

        for indx, val in enumerate(ar):
            if indx != mid:
                if val[0] < pivot[0]:
                    smaller.append(val)
                elif val[0] > pivot[0]:
                    greater.append(val)

                else:
                    if indx < mid:
                        smaller.append(val)
                    else:
                        greater.append(val)
        return quickSort(smaller) + [pivot] + quickSort(greater)


def quick_sort_ranges(T, p, r):
    # if p < r:
    #     q = partition(T, p, r)
    #     quick_sort(T, p, q - 1)
    #     quick_sort(T, q + 1, r)

    # to avoid two recursions problem
    while p < r:
        q = partition_ranges(T, p, r)
        quick_sort_ranges(T, p, q - 1)
        p = q + 1


def partition_ranges(T, p, r):

    randpivot = randint(p, r)
    T[randpivot], T[r] = T[r], T[randpivot]
    x = T[r][1] - T[r][0]  # to avoid getting O(n^2) we can set a value of x to random from < T[p] .. T[r] >
    i = p - 1
    for j in range(p, r):
        if T[j][1] - T[j][0] > x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def mergesort(L):
    if len(L) > 1:
        v = len(L) // 2
        l = L[:v]
        r = L[v:]
        mergesort(l)
        mergesort(r)
        merge(L, l, r)


def merge(L, l, r):
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i][0] < r[j][0] or (l[i][0] == r[j][0] and l[i][1] >= r[j][1]):
            L[k] = l[i]
            i += 1
        else:
            L[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        L[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        L[k] = r[j]
        j += 1
        k += 1

"""
sortuję tablicę L dwa razy, najpierw ze względu na wielkości przedziałów, potem (stabilnym quick sortem) ze względu na 
początki przedziałów. następnie sprawdzam, ile przedziałów należy do aktualnego rozpatrywanego przedziału (p) 
(rozpatruje tylko te przedziały, których początek jest mniejszy od końca przedziału p). następnie aktualizuje p albo
za pomocą przedziału który wcześniej nie zmieścił się w p albo za pomocą ostatniego q
"""


def depth(L):

    # XD
    # max_index = -1
    # maximum = 0
    #
    # for i in range(len(L)):
    #     if L[i][1] - L[i][0] > maximum:
    #         maximum = L[i][1] - L[i][0]
    #         max_index = i
    #
    # a = L[max_index][0]
    # b = L[max_index][1]
    #
    # counter = 0
    #
    # for i in range(len(L)):
    #     if i == max_index:
    #         continue
    #     if L[i][0] >= a and L[i][1] <= b:
    #         counter += 1
    #
    # return counter

    mergesort(L)

    p = 0
    result = 0

    while p < len(L):
        flag = True
        current = 0
        q = p + 1
        while q < len(L) and L[q][0] < L[p][1]:
            if L[q][1] <= L[p][1]:
                current += 1
            if flag and L[q][1] > L[p][1]:
                flag = False
                new_start = q
            q += 1

        if flag:
            p = q
        else:
            p = new_start

        if current > result:
            result = current

        # while p + 1 < len(tab) and tab[p][0] == tab[p + 1][0]:
        #     p += 1
        # p += 1

    return result


runtests(depth)
