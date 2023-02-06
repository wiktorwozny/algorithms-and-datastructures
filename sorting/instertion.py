def insertion_sort(T):  # O(n^2), very little memory needed
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


tab = [7, 8, 5, 2, 4, 6, 3]
print(tab)
insertion_sort(tab)
print(tab)
