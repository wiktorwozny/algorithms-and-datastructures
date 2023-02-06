# Wiktor Woźny 410434
# tworzę N bucketów, każdy napis wrzucam do odpowiedniego bucketa (indeks bucketa wyznacza mi długość napisu), w ten
# sposób będę porównywał ze sobą tylko napisy o tej samej długości, do bucketów razem ze słowem dopisuje numer 0, który
# oznacza, że napis jeszcze nie był porównywany, potem zmieniam go na 1 co oznacza, że ten napis był już porównywany i
# nie ma sensu sprawdzać porównywać go z innymi. Złożoność pamięciowa - O(N), Złożoność czasowa - O(n^2)


from kol1atesty import runtests


def get_index(ch):
    return ord(ch) - 97


def radixsort_strings(T, length):

    n = len(T)
    for i in range(length):
        counts = [0] * 26
        output = [0] * n
        for word in T:
            counts[get_index(word[-(i + 1)])] += 1

        for j in range(1, 26):
            counts[j] += counts[j - 1]

        for j in range(n - 1, -1, -1):
            output[counts[get_index(T[j][-(i + 1)])] - 1] = T[j]
            counts[get_index(T[j][-(i + 1)])] -= 1

        for j in range(n):
            T[j] = output[j]

    # print(T)


def normalize(string):

    mid = len(string) // 2
    for i in range(mid):
        if ord(string[i]) > ord(string[-(i + 1)]):
            return string[::-1]
        elif ord(string[i]) < ord(string[-(i + 1)]):
            return string

    return string


def g(T):

    for i in range(len(T)):
        T[i] = normalize(T[i])

    result = 0
    maximum = 0
    # counts = [0] * 26
    for str in T:
        maximum = max(len(str), maximum)

    # n = len(T)
    buckets = [[] for _ in range(maximum)]

    for string in T:
        index = len(string) - 1
        buckets[index].append(string)

    for i in range(maximum):
        if len(buckets[i]) < 2:
            continue
        # if len(buckets[i]) <= result:
        #     continue

        radixsort_strings(buckets[i], i + 1)

    for i in range(maximum):
        if len(buckets[i]) < 2:
            continue
        if len(buckets[i]) <= result:
            continue

        counter = 1
        for x in range(1, len(buckets[i])):
            if buckets[i][x] == buckets[i][x - 1]:
                counter += 1
            else:
                counter = 1

            result = max(result, counter)

        # x = 0
        # while x < len(buckets[i]):
        #     word = buckets[i][x][0]
        #     reversed = word[::-1]
        #     counter = 1
        #
        #     if buckets[i][x][1] == 0:
        #         buckets[i][x][1] = 1
        #         y = x + 1
        #         while y < len(buckets[i]):
        #             if buckets[i][y][1] == 0 and (buckets[i][y][0] == word or buckets[i][y][0] == reversed):
        #                 buckets[i][y][1] = 1
        #                 counter += 1
        #             y += 1
        #
        #     x += 1
        #     result = max(counter, result)

    return result


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
