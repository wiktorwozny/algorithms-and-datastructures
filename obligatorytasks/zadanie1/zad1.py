from zad1testy import Node, runtests


def left(i): return (2 * i) + 1
def right(i): return (2 * i) + 2
def parent(i): return (i - 1) // 2


def build_min_heap(A):

    n = len(A)

    for i in range(parent(n - 1), -1, -1):
        min_heapify(A, n, i)


def min_heapify(A, n, i):

    l = left(i)
    r = right(i)
    min_index = i

    if l < n and A[min_index].val > A[l].val:
        min_index = l
    if r < n and A[min_index].val > A[r].val:
        min_index = r
    if min_index != i:
        A[i], A[min_index] = A[min_index], A[i]
        min_heapify(A, n, min_index)


def insertion_sort(arr):  # O(n^2), very little memory needed
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j].val > key.val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


'''
w pierwszej części zadania przepisuję node'y linked listy do tablicy, aby potem zbudować kopiec z k + 1 elementów,
ponieważ wiemy, że elementy są oddalone od swojego docelowego miejsca o najwyżej k. Buduję kopiec t rosnący, pod 
indeksem 0 znajduje się najmniejszy element i ten element co iteracje pętli zewnętrznej przepinamy do poprzedniego 
elementu q, zamieniamy go w kopcu z następnym elementem tablicy t i naprawiamy kopiec. Następnie, gdy nie ma już 
możliwości dobierania elementów z tablicy sortuję resztę i dopinam do listy
'''


def SortH(p, k):

    t = []
    q = p
    while q is not None:
        t.append(q)
        q = q.next

    if k > len(t):
        k = len(t)

    if k == 1:  # dla k = 1 najbardziej oplacalny wydaje sie insertion sort
        insertion_sort(t)

        p = t[0]
        q = p
        for i in range(1, len(t)):
            q.next = t[i]
            q = q.next

        q.next = None

        return p


    '''  bez appenda ale za wolne 
    q = p
    n = 0
    while q is not None:
        q = q.next
        n += 1

    t = [0 for i in range(n)]
    q = p
    for i in range(n):
        t[i] = q
        q = q.next
    '''

    heap = t[:k + 1]
    build_min_heap(heap)  # budujemy kopiec o długości k + 1
    p = heap[0]  # wiedząc, że najmniejszy element listy znajduje się w odległości co najwyżej K od początku listy,
    # przypisujemy
    q = p

    for index in range(k + 1, len(t)):
        heap[0] = heap[-1]
        min_heapify(heap, k, 0)
        heap[-1] = t[index]

        a = parent(k)
        b = k

        while a >= 0 and heap[a].val > heap[b].val:
            heap[b], heap[a] = heap[a], heap[b]
            temp = a
            a = parent(a)
            b = temp

        q.next = heap[0]
        q = q.next

    insertion_sort(heap)  # sortuję resztę elementów i uzupełniam listę końcową
    for i in range(len(heap)):
        q.next = heap[i]
        q = q.next

    q.next = None

    return p


runtests(SortH)
