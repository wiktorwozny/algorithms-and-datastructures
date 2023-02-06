class Node:
    def __init__(self, v):
        self.val = v
        self.next = None


class Zbior:
    def __init__(self):
        self.first = None


def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range(n - 1, -1, -1):
        tmp = Node(tab[i])
        tmp.next = first
        first = tmp
    return first


def print_linked_list(first):
    while first is not None:
        print(' -->', first.val, end='')
        first = first.next
    return first


def split(L):  # seperates the sub_list in growing order and returns new beggining of the list

    while L.next is not None and L.val <= L.next.val:
        L = L.next

    res = L.next
    L.next = None

    return res


def tail(L):  # returns the last element in ll

    while L.next is not None:
        L = L.next

    return L


def merge(A, B):  # merges two linked lists

    C = Node(None)
    D = C

    while True:
        if A is None:
            D.next = B
            return C.next, tail(B)

        if B is None:
            D.next = A
            return C.next, tail(A)

        if A.val <= B.val:
            D.next = A
            A = A.next

        else:
            D.next = B
            B = B.next

        D = D.next


def merge_sort_ll(L):  # sorting ll

    T = tail(L)

    while True:
        A = L
        L = split(L)

        if L is None:  # L is None means that we splited the list into only one piece so the list was sorted
            return A

        B = L
        L = split(L)
        C, D = merge(A, B)

        if L is None:  # same thing here
            return C

        T.next = C
        T = D


linked = make_linked_list([2, 6, 3, 1, 7, 2, 6, 4, 9, 2, 4, 1, 6])
merge_sort_ll(linked)
print_linked_list(linked)
