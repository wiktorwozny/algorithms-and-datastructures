def counting_sort(T, k):  # complexity O(n + k) where n is size of the array, we can sort numbers from [0 .. k]

    n = len(T)
    # k = max(T)  # if the range is not given
    counts = [0] * k
    output = [0] * n

    for x in T:
        counts[x] += 1

    for i in range(1, k):
        counts[i] += counts[i - 1]

    for i in range(n - 1, -1, -1):
        output[counts[T[i]] - 1] = T[i]
        counts[T[i]] -= 1

    for i in range(n):
        T[i] = output[i]


# tab = [3, 6, 2, 7, 1, 8, 3, 0, 3]
# print(tab)
# print(counting_sort(tab, 9))


def radix_sort(A, d):  # sorting d-digits numbers

    for k in range(1, d+1):
        power_10 = 1 * (10 ** (k-1))
        C = [0] * 10
        B = [0] * len(A)

        for i in range(len(A)):
            C[(A[i] % 10 ** k) // power_10] += 1

        for i in range(1, 10):
            C[i] = C[i - 1] + C[i]

        for j in range(len(A)-1,-1,-1):
            B[C[(A[j] % 10 ** k) // power_10]-1] = A[j]
            C[(A[j] % 10 ** k) // power_10] = C[(A[j] % 10 ** k) // power_10] - 1

        A = B

    return A


def insertion_sort(T):  # O(n^2), very little memory needed
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


def bucket_sort(A):

    n = len(A)
    buckets = [[] for _ in range(n + 1)]
    maximum = max(A)

    for i in range(n):
        index = int((A[i] / maximum) * n)
        buckets[index].append(A[i])

    for i in range(n):
        insertion_sort(buckets[i])

    a = 0
    for i in range(n + 1):
        for j in range(len(buckets[i])):
            A[a] = buckets[i][j]
            a += 1

    return A


# tab = [1, 2, 5, 3, 8, 5, 11, 16, 19, 13]
# tab = bucket_sort(tab)
# print(tab)


def bucked_sort_range(A, x, y):

    n = len(A)
    buckets = [[] for _ in range(n + 1)]

    for i in range(n):
        index = int(((A[i] - x) / (y - x)) * n)
        buckets[index].append(A[i])

    for i in range(len(buckets)):
        insertion_sort(buckets[i])

    a = 0
    for i in range(n + 1):
        for j in range(len(buckets[i])):
            A[a] = buckets[i][j]
            a += 1

    return A


tab = [5, 7, 18, 15, 12, 10, 20]
print(bucked_sort_range(tab, 5, 20))
