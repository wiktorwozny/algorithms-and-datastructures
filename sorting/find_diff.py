def find_diff(t, diff):  # finding two index (i, j) in sorted tab t that t[j] - t[i] = diff

    i = j = 0
    while j < len(t):
        if t[j] - t[i] == diff:
            return i, j
        elif t[j] - t[i] < diff:
            j += 1
        else:
            i += 1

    return False  # returning False if difference does not exist


tab = [1, 5, 6, 10, 12, 15, 16]
print(find_diff(tab, 34))
