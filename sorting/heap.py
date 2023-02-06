def left(i): return (2 * i) + 1
def right(i): return (2 * i) + 2
def parent(i): return (i - 1) // 2


def heapify(A, n, i):

    l = left(i)
    r = right(i)
    max_index = i

    if l < n and A[max_index] < A[l]:
        max_index = l
    if r < n and A[max_index] < A[r]:
        max_index = r
    if max_index != i:
        A[i], A[max_index] = A[max_index], A[i]
        heapify(A, n, max_index)


def min_heapify(A, n, i):

    l = left(i)
    r = right(i)
    max_index = i

    if l < n and A[max_index] > A[l]:
        max_index = l
    if r < n and A[max_index] > A[r]:
        max_index = r
    if max_index != i:
        A[i], A[max_index] = A[max_index], A[i]
        min_heapify(A, n, max_index)


def build_heap(A):

    n = len(A)

    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def build_min_heap(A):

    n = len(A)

    for i in range(parent(n - 1), -1, -1):
        min_heapify(A, n, i)


def heap_sort(A):  # O(nlogn)

    n = len(A)
    build_heap(A)

    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


# tab = [1, 5, 7, 2, 8, 12, 74, 2, 1, 32, 79, 32, 15, 74, 32, 15, 2, 7, 96, 35, 2, 12]
# print(tab[:3])
# print(tab[3])
# print("main: ", tab)
# print()
# build_heap(tab)
# print(tab)
# tab = [1, 5, 7, 2, 8, 12, 74, 2, 1, 32, 79, 32, 15, 74, 32, 15, 2, 7, 96, 35, 2, 12]
# build_min_heap(tab)
# print(tab)
tab = [33, 33, 6, 90, 33, 32, 31, 91, 90, 89, 50]
min_heapify(tab, len(tab), 0)
print(tab)

#print(tab)
#heap_sort(tab)
#print(tab)
