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


def insert(L, n):  # inserting node into the sorted list with guardian

    while L.next is not None and L.next.val < n.val:
        L = L.next

    temp = n
    temp.next = L.next
    L.next = temp


def insertion_sort_linked(L):  # sorting linked list

    res = Node(None)  # creating new list

    while L.next is not None:
        k = L.next
        L.next = L.next.next
        insert(res, k)
        
    L.next = res.next
