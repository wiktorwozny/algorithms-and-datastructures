def bubble_sort(T):  # O(n^2), very little memory

    n = len(T)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if T[j + 1] < T[j]:
                T[j], T[j + 1] = T[j + 1], T[j]


tab = [1, 0, 3, 2, 4, 6, 5]
print(tab)
bubble_sort(tab)
print(tab)
