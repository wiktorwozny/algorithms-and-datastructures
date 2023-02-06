def merge(T):  # O(nlogn), recursion

    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        # print("L: ", L)
        # print("R: ", R)
        merge(L)
        merge(R)

        i = j = k = 0  # variables appropriately for left side (L), right side (R), main tab

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1
        # print("po: ", T)


tab = [3, 1, 5, 2, 7, 8, 2]
print(tab)
merge(tab)
print(tab)
