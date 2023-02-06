def selection_sort(T):  # O(n^2)

    for i in range(len(T) - 1):
        minIndex = i
        for j in range(i + 1, len(T)):
            if T[j] < T[minIndex]:
                minIndex = j
        T[i], T[minIndex] = T[minIndex], T[i]


tab = [8, 2, 1, 9, 5]
print(tab)
selection_sort(tab)
print(tab)
