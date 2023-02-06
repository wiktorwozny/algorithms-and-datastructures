#  QUICK SORT

class Stack:  # stack implementation using class

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, x):
        return self.items.append(x)

    def pop(self):
        return self.items.pop()

    def state(self):
        if len(self.items) == 0:
            return "Stack is empty"
        else:
            return len(self.items)


def quick_sort(T, p, r):

    if p < r:
        q = partition(T, p, r)
        quick_sort(T, p, q - 1)
        quick_sort(T, q + 1, r)

    # to avoid two recursions problem
    # while p < r:
    #     q = partition(T, p, r)
    #     quick_sort(T, p, q - 1)
    #     p = q + 1


def partition(T, p, r):

    x = T[r]  # to avoid getting O(n^2) we can set a value of x to random from < T[p] .. T[r] >, x = T[randint(0,
    # len(T)]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quick_sort_lessmemory(T, p, r):  # O(logn) memory, taking smaller part of the array after partition

    while p < r:
        q = partition(T, p, r)
        if (q - p) < (r - q):
            quick_sort_lessmemory(T, p, q - 1)
        else:
            quick_sort_lessmemory(T, q + 1, r)
            r = q - 1


def quick_sort_ownstack(T, p, r):  # iteration version of quick sort with own stack implemented above ( O(logn)
    # memory as well )

    S = Stack()
    S.push((p, r))
    while not S.isEmpty():
        p, r = S.pop()
        if p < r:
            q = partition(T, p, r)
            if (q - p) < (r - q):
                # here we push to the stack smaller part of array (after the partition) as a
                # second, so in the line after while loop we instantly pop the smaller part of the array to get O(logn)
                # memory
                S.push((q + 1, r))
                S.push((p, q - 1))
            else:
                S.push((p, q - 1))
                S.push((q + 1, r))


#  problem: chcemy obliczyć który element po posortowaniu będzie pod indeksem k

def select(T, p, k, r):

    if p == r:
        return T[p]
    if p < r:
        q = partition(T, p, r)
        if q == k:
            return T[q]
        elif q < k:
            return select(T, q + 1, k, r)
        else:
            return select(T, p, k, q - 1)


"""
algorytm magicznych piątek:
1) podzielenie wejściowej tablicy na ~ n/5 grup, każda po 5 elementów, w każdej tej grupie wyznaczamy medianę
2) rekurencyjnie wyznaczamy x jako medianę median
3) kontunuujemy tak jak w funkcji select, traktując x jako piwot (q)
"""

tab = [2, 5, 2, 7, 4, 6, 2, 7, 9, 1, 42, 32, 12, 54]
print(tab)
quick_sort_ownstack(tab, 0, len(tab) - 1)
print(tab)
