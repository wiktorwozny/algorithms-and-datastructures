# Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x2 + y2 <= k, które są w nim
# równomiernie rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze jest proporcjonalne do pola tego
# obszaru.Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0),
# tzn. d = sqrt(x2 + y2).
from math import sqrt
from random import randint
from math import log


def distance(tuple):
    return sqrt(tuple[0] * tuple[0] + tuple[1] * tuple[1])


def insertion_sort_distances(T):  # O(n^2), very little memory needed
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and distance(T[j]) > distance(key):
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


def kulko(tab, k):

    n = len(tab)
    buckets = [[] for _ in range(n + 1)]

    for i in range(n):
        d = distance(tab[i])
        index = int((d / k) * n)
        buckets[index].append(tab[i])

    for i in range(n + 1):
        insertion_sort_distances(buckets[i])

    a = 0
    for i in range(n + 1):
        for j in range(len(buckets[i])):
            tab[a] = buckets[i][j]
            a += 1

    return tab


# arr = [[2, 3], [1, 6], [5, 8], [2, 5], [-2, -6], [-1, -3], [3, 12]]
# print(kulko(arr, 13))


# Mamy daną tablicę A z n liczbami naturalnymi. Proszę zaproponować algorytm o złożoności O(n), który stwierdza,
# czy w tablicy ponad połowa elementów ma jednakową wartość.

def leader(tab):

    w = tab[0]
    c = 1

    for i in range(1, len(tab)):
        if tab[i] == w:
            c += 1
        elif tab[i] != w:
            c -= 1
        if c < 0:
            w = tab[i]
            c = 1

    counter = 0

    for i in range(len(tab)):
        if tab[i] == w:
            counter += 1

    if counter > len(tab) // 2:
        return True, w
    else:
        return False


# arr = [1, 2, 3, 2, 2, 3, 2]
# print(leader(arr))


# Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej tablicy
# na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który posortuje tablicę w
# czasie O(n).


def insertion_sort(T):  # O(n^2), very little memory needed
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


def sort_ch(tab, k):

    n = len(tab)
    buckets = [[] for _ in range(n + 3)]

    for i in range(n):
        if tab[i] < 0:
            buckets[0].append(tab[i])
        elif tab[i] > k:
            buckets[-1].append(tab[i])
        else:
            index = int((tab[i] / k) * n) + 1
            buckets[index].append(tab[i])

    for i in range(n + 3):
        insertion_sort(buckets[i])

    a = 0
    for i in range(n + 3):
        for j in range(len(buckets[i])):
            tab[a] = buckets[i][j]
            a += 1

    return tab


# arr = [2, 4, 6, 456, 7, 0, 200, 5, -100, 10, 500, -500, 8, 9, 1]
# print(sort_ch(arr, 10))


# Dana jest klasa
#
# class Node:
# val = 0
# next = None
#
# reprezentująca węzeł jednokierunkowego łańcucha odsyłaczowego, w którym wartości val poszczególnych węzłów zostały
# wygenerowane zgodnie z rozkładem jednostajnym na przedziale [a, b].
# Napisz procedurę sort(first), która sortuje taką listę. Funkcja powinna być jak najszybsza.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


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


def insertion_sort_linked(T):  # O(n^2), very little memory needed
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j].val > key.val:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


def bucket_sort_linked(head, a, b):

    p = head
    n = 0

    while p.next is not None:
        n += 1
        p = p.next

    buckets = [[] for _ in range(n + 1)]
    p = head

    while p is not None:
        index = int(((p.val - a) / (b - a)) * n)
        buckets[index].append(p)
        p = p.next

    for i in range(n + 1):
        insertion_sort_linked(buckets[i])

    a = 0
    while len(buckets[a]) == 0:
        a += 1

    head = buckets[a][0]
    p = head
    for i in range(1, len(buckets[a])):
        p.next = buckets[a][i]
        p = p.next

    for i in range(a, n + 1):
        for j in range(len(buckets[i])):
            p.next = buckets[i][j]
            p = p.next

    p.next = None

    return head


# arr = [13, 29, 46, 48, 100, 56, 74, 29, 73, 52, 38, 49, 26, 5, 88, 59, 72, 4, 44, 12, 76, 27, 11, 85, 22, 24, 40, 64,
#        25, 90, 50, 90, 89]
#
# print_linked_list(bucket_sort_linked(make_linked_list(arr), 0, 100))

# Proszę podać algorytm sortujący n elementową tablicę ze zbioru liczb [0, ..., n^2 - 1]

def change(x, n):

    i = x % n
    x //= n
    j = x % n

    return j, i


def sortn(T):

    n = len(T)
    for i in range(n):
        T[i] = change(T[i], n)

    counts = [0] * n
    output = [0] * n
    for i in range(n):
        counts[T[i][1]] += 1

    for i in range(1, n):
        counts[i] += counts[i - 1]

    for i in range(n - 1, -1, -1):
        output[counts[T[i][1]] - 1] = T[i]
        counts[T[i][1]] -= 1

    T = output
    counts = [0] * n
    output = [0] * n

    for i in range(n):
        counts[T[i][0]] += 1

    for i in range(1, n):
        counts[i] += counts[i - 1]

    for i in range(n - 1, -1, -1):
        output[counts[T[i][0]] - 1] = T[i]
        counts[T[i][0]] -= 1

    T = output
    for i in range(n):
        sum = T[i][1] + T[i][0] * n
        T[i] = sum

    return T


# print(sortn([54, 23, 74, 21, 24, 9, 21, 56, 86, 91, 120, 32, 53]))

# Zadanie jak powyżej, ale tablica T zawiera elementy ze zbioru A, gdzie |A| <= logn

def logsort(T):

    # k = int(log(len(T), 2))
    counts = [[T[0], 1]]

    for i in range(1, len(T)):
        x = T[i]
        l = 0
        r = len(counts) - 1
        flag = True
        while r >= l:
            mid = (l + r) // 2

            if counts[mid][0] == x:
                counts[mid][1] += 1
                flag = False
                break

            elif counts[mid][0] > x:
                r = mid - 1

            else:
                l = mid + 1

        if flag:
            counts = counts[:r + 1] + [[T[i], 1]] + counts[l:]

    j = 0
    for i in range(len(counts)):
        while counts[i][1] > 0:
            T[j] = counts[i][0]
            counts[i][1] -= 1
            j += 1

    return T


# print(logsort([23, 4, 54, 23, 54, 4, 4, 4, 54]))


# mamy k kolorów w tablicy (kolory oznaczamy kolejno numerami 0, 1, ..., k), chcemy znaleźć najkrótszy podciąg
# zawierający wszystkie kolory


def colors(T, k):

    C = [0] * k
    empty = k
    l = 0
    r = 0
    min_len = len(T) + 1
    while r < len(T):
        while empty > 0:
            if r == len(T):
                break
            if C[T[r]] == 0:
                empty -= 1
            C[T[r]] += 1
            r += 1

        curr_len = r - l
        min_len = min(min_len, curr_len)
        while empty == 0:
            if C[T[l]] == 1:
                C[T[l]] = 0
                l += 1
                empty += 1
                break
            C[T[l]] -= 1
            l += 1
            curr_len -= 1
            min_len = min(min_len, curr_len)

    return min_len


# print(colors([3, 1, 1, 1, 0, 2, 2, 1, 1, 2, 3, 3, 3, 1, 3, 1, 3], 4))


# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.


def mergesort(T):

    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        mergesort(L)
        mergesort(R)
        merge(T, L, R)


def merge(T, L, R):

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i][0] > R[j][0] or (L[i][0] == R[j][0] and L[i][1] <= R[j][1]):
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


def pretty_sort(T):

    n = len(T)

    for i in range(n):
        num = T[i]
        data = [0, 0, num]
        digits = [0] * 10
        while num > 0:
            if digits[num % 10] == 0:
                data[0] += 1
                digits[num % 10] = 1
            elif digits[num % 10] == 1:
                data[0] -= 1
                data[1] += 1
                digits[num % 10] = 2

            num //= 10

        T[i] = data

    # mergesort(T)

    counts = [0] * 10
    output = [0] * n

    for x in T:
        counts[x[1]] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    for i in range(n - 1, -1, -1):
        output[counts[T[i][1]] - 1] = T[i]
        counts[T[i][1]] -= 1

    for i in range(n):
        T[i] = output[i]

    print(T)

    counts = [0] * 10
    output = [0] * n

    for x in T:
        counts[x[0]] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    for i in range(n):
        output[-(counts[T[i][0]])] = T[i][2]
        counts[T[i][0]] -= 1

    for i in range(n):
        T[i] = output[i]

    # for i in range(len(T)):
    #     T[i] = T[i][2]

    return T


# print(pretty_sort([123, 455, 1266, 114577, 2344, 67333, 123456789, 5264435, 12312, 5352]))


# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.


def section(T, p, q):

    a = 150  # zakładam, że wzrosty żołnierzy należą do przedziału [150 .. 220]
    b = 220
    n = len(T)

    buckets = [[] for _ in range(n + 1)]
    for i in range(n):
        index = int(((T[i] - a) / (b - a)) * n)
        buckets[index].append(T[i])

    a = 0
    for i in range(n + 1):
        for j in range(len(buckets[i])):
            T[a] = buckets[i][j]
            a += 1

    insertion_sort(T)

    return T[p:q + 1]


# print(section([168, 201, 199, 180, 185, 170, 176, 188, 174], 0, 5))


# Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, gdzie m jest znacznie mniejsze od n. Zaproponuj
# algorytm, który sprawdzi, czy zbiory są rozłączne.

def partition(T, p, r):

    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


def quicksort(T, p, r):

    while p < r:
        q = partition(T, p, r)
        quicksort(T, p, q - 1)
        p = q + 1


def sets(A, B):

    m = len(B)

    quicksort(B, 0, m - 1)

    for x in A:
        l = 0
        r = m - 1
        while r >= l:
            mid = (l + r) // 2

            if B[mid] == x:
                return False

            elif B[mid] > x:
                r = mid - 1

            else:
                l = mid + 1

    return True


# A = [43, 23, 15, 74, 12, 42, 45, 78, 52, 1, 2, 5, 3, 6, 9, 43, 23, 13, 23, 98, 54, 23, 12, 32, 76, 0, 54, 2, 1, 86, 43]
# B = [8, 999, 123, 63]
# print(sets(A, B))


# Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algorytm, który podzieli te liczby na n par w taki sposób, że
# podział będzie miał najmniejszą maksymalną sumę liczb w parze. Przykładowo, dla liczb     (1, 3, 5, 9) możemy mieć
# podziały ((1,3),(5,9)), ((1,5),(3,9)), oraz ((1,9),(3,5)). Sumy par dla tych podziałów to (4, 14), (6, 12) oraz
# (10, 8), w związku z tym maksymalne sumy to 14, 12 oraz 10. Wynika z tego, że ostatni podział ma najmniejszą
# maksymalną sumę.

def pairs(T):

    quicksort(T, 0, len(T) - 1)

    output = [[0, 0] for _ in range(len(T) // 2)]

    for i in range((len(T) // 2)):
        output[i][0] = T[i]
        output[i][1] = T[-(i + 1)]

    return output


# print(pairs([5, 3, 7, 2, 8, 2, 3, 39, 2, 34, 6, 2]))

# Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne, a reszta tablicy ma
# wartości None. Nie jest dana wartość n. Przedstaw algorytm, który dla danej liczby naturalnej x znajdzie indeks w
# tablicy, pod którym znajduje się wartość x. Jeżeli nie ma jej w tablicy, to należy zwrócić None.

def inftab(T, x):

    prev = 0
    curr = 1

    while T[curr] is not None and T[curr] <= x:
        prev, curr = curr, curr * 2

    l = prev
    r = curr
    while r >= l:
        if T[l] is None:
            return None
        mid = (l + r) // 2

        if T[mid] == x:
            return mid

        elif T[mid] is None or T[mid] > x:
            r = mid - 1

        else:
            l = mid + 1

    return None


# tab = [None] * (10*100)
# n = 20
# for i in range(n):
#     tab[i] = randint(1, 26)
#
# quicksort(tab, 0, n - 1)
# print(tab[:n + 2])
# print(inftab(tab, 20))


# Dana jest posortowana rosnąco tablica A wielkości n zawierająca parami różne liczby naturalne. Podaj algorytm, który
# sprawdzi, czy jest taki indeks i, że A[i] == i.
#
# Co zmieni się, jeżeli liczby będą po prostu całkowite, niekoniecznie naturalne? (dla naturalnych wystarczy sprawdzić
# czy A[0] == 0, więc od razu zrobię dla całkowitych)

def smilingface(A):

    l = 0
    r = len(A) - 1

    while r >= l:
        mid = (l + r) // 2

        if A[mid] == mid:
            return True, mid

        elif A[mid] > mid:
            r = mid - 1

        else:
            l = mid + 1

    return False


# tab = [-9, -4, -2, -1, 0, 2, 5, 5, 9, 11]
# print(smilingface(tab))

# Dane są trzy zbiory reprezentowane przez tablice: A, B i C. Napisz algorytm, który powie, czy istnieje taka trójka
# a, b, c z odpowiednio A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników!

def sumka(A, B, C):

    quicksort(A, 0, len(A) - 1)
    quicksort(B, 0, len(B) - 1)

    # print(A)
    # print(B)

    for i in range(len(C)):
        a = 0
        b = len(B) - 1
        sum = A[a] + B[b]

        while sum != C[i] and a < len(A) and b >= 0:
            sum = A[a] + B[b]
            if sum < C[i]:
                a += 1
            else:
                b -= 1

        if sum == C[i]:
            return True

        while a < len(A):
            sum = A[a] + B[b + 1]
            a += 1
            if sum == C[i]:
                return True

        while b >= 0:
            sum = A[a - 1] + B[b]
            b -= 1
            if sum == C[i]:
                return True

    return False


# A = [0, 2, 3, 4, 5, 6, 7, 8, 9]
# B = [5, 7, 21, 32, 12, 18, 2, 6]
# C = [10]
#
# print(sumka(A, B, C))

# sortowanie stringuw

def find_index(ch):
    return ord(ch) - 97


def sort_string(A):

    m = 0
    n = float("inf")

    for string in A:
        m = max(m, len(string))
        n = min(n, len(string))

    diff = m - n + 1

    B = [[] for _ in range(diff)]

    for i in range(len(A)):
        index = len(A[i]) - n
        B[index].append(A[i])

    for i in range(len(B)):
        if B[i] == []:
            continue

        for k in range(len(B[i])):
            for x in range(len(B[i]) - 1, -1, -1):
                counts = [0] * 26
                output = [0] * len(B[i])

                for y in B[i]:
                    counts[find_index(y[x])] += 1

                for y in range(1, 26):
                    counts[y] += counts[y - 1]

                for y in range(len(B[i]) - 1, -1, -1):
                    output[counts[find_index(B[i][y][x])] - 1] = B[i][y]
                    counts[find_index(B[i][y][x])] -= 1

                for y in range(len(B[i])):
                    B[i][y] = output[y]

    print(B)
    return


# tab = ['ala','ul','kasia', 'piotrek','radek', 'gruby','ola', 'natalia','grzes','qn']
# sort_string(tab)


# Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
# są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
# aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
# a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
# Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
# jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
# podać złożoność czasową i pamięciową zaproponowanego algorytmu.

def partition_dwuwymiarowka(T, p, r):

    n = len(T)
    x = T[r//n][r%n]
    i = p - 1
    for j in range(p, r):
        if T[j//n][j%n] <= x:
            i += 1
            T[i//n][i%n], T[j//n][j%n] = T[j//n][j%n], T[i//n][i%n]

    T[(i + 1)//n][(i + 1)%n], T[r//n][r%n] = T[r//n][r%n], T[(i + 1)//n][(i + 1)%n]

    return i + 1


def quickselect_dwuwymiarowka(T, p, r, k):

    n = len(T)
    if p == r:
        return T[p//n][p%n]

    if p < r:
        q = partition_dwuwymiarowka(T, p, r)
        if q == k:
            return T[q//n][q%n]
        elif q < k:
            return quickselect_dwuwymiarowka(T, q + 1, r, k)
        else:
            return quickselect_dwuwymiarowka(T, p, q - 1, k)


def median(T):

    n = len(T)
    output = [[0] * n for _ in range(n)]
    m = n * n - 1
    minmedian = quickselect_dwuwymiarowka(T, 0, m, (n*n)//2 - n//2)
    maxmedian = quickselect_dwuwymiarowka(T, 0, m, ((n*n)//2 + n//2) - 1)

    x = 0
    row_up = 0
    col_up = 1
    row_down = 1
    col_down = 0
    # flag = True
    for i in range(n * n):
        val = T[i//n][i%n]
        if minmedian <= val <= maxmedian:
            output[x][x] = val
            x += 1
            # if x == n:
            #     flag = False
        elif val < minmedian:
            if row_down == n:
                col_down += 1
                row_down = col_down + 1
            output[row_down][col_down] = val
            row_down += 1
        else:
            if col_up == n:
                row_up += 1
                col_up = row_up + 1
            output[row_up][col_up] = val
            col_up += 1

    return output


# T = [[43, 74, 53, 97], [80, 61, 61, 19], [61, 73, 89, 93], [42, 17, 89, 80]]
# print(median(T))
# a chuj z nim dziala dla parami roznych

