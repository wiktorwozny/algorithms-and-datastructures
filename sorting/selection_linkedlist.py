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


def delete_max(L):  # deleting and returning the maximum element in linked list (unsorted)

    max_L = L  # link to the maximum element

    while L.next is not None:
        if L.next.val > max_L.next.val:
            max_L = L
        L = L.next

    res = max_L.next
    max_L.next = max_L.next.next
    return res


def selectionsort_linked(L):  # sorting linked list

    res = Node(None)

    while L.next is not None:
        temp = delete_max(L)
        temp.next = res.next
        res.next = temp
    
    L.next = res.next
