# Wiktor Woźny 410434

# zadanie sprowadza się do rozwiązania algorytmem djikstry, który jest o złożoności O(ElogV), tak samo jak mój program
# na początku tworzę nowy graf, w postaci list sąsiedztwa, bo to moja ulubiona postać prezentowania grafu, co więcej
# dla algorytmu djikstry wychodzi wtedy mniejsza złożoność niż w przypadku postaci macierzowej, a przynajmniej tak mi
# się wydaje, po stworzeniu grafu do kolejki wrzucam wierzchołek a z odległością 0 (odległość jest na pierwszym indeksie
# w krotce żeby PriorityQueue ładnie działało) i wykonuje się jak najbardziej typowy algorytm djikstry, na początku
# zawsze sprawdzam czy wyciągnięty wierzołek u z kolejki nie jest czasem wierzchołkiem b, jeżeli jest to zwracam od razu
# odległość od a do b, bo jak wiemy z twierdzenia z wykładu, wierzchołek u gdy jest wyciągnięty z kolejki to d zawiera
# długość najkrótszej ścieżki do u, jeżeli u nie jest b, to wykonuje najzwyklejszą relaksację, potem sprawdzam czy u
# nie jest czasem w tablicy S, jeżeli jest to dodaję nieodwiedzone wierzchołki v należące do S z wagą d, czyli taką
# samą jaką miał wierzchołek u (to ma symulować teleportację), jeżeli wszystkie wierzchołki z kolejki zostaną
# przetworzone i nie stało się tak, żeby u == b to zwracam None bo to znaczy że nie istnieje ścieżka z a do b.
# Czyli podsumowując, chyba działa, przynajmniej na testach, złożoność O(mlogn + m) (to + m z takiego powodu, że tyle
# zajmuje tworzenie grafu), złożoność pamięciowa O(m ^ 2 + 3n), przynajmniej coś takiego, trochę nie rozumiem
# podpowiedzi i jej nie użyłem nie wiem czy to źle


from kol3atesty import runtests
from math import inf
from queue import PriorityQueue as PQ


def relax(distances, d, v, w):

    if distances[v] > d + w:
        distances[v] = d + w
        return True

    return False


def spacetravel(n, E, S, a, b):

    G = [[] for _ in range(n)]
    for u, v, w in E:
        G[u].append([v, w])
        G[v].append([u, w])

    visited = [False for _ in range(n)]
    distances = [inf for _ in range(n)]
    queue = PQ()

    queue.put((0, a, 1))  # 2 indeks czy juz wykorzystalismy warunek
    distances[a] = 0

    while not queue.empty():
        d, u, warunek = queue.get()

        if u == b:
            return d

        for v, w in G[u]:
            if not visited[v]:
                if relax(distances, d, v, w):
                    queue.put((d + w, v, warunek))

        if warunek:
            if u in S:
                for v in S:
                    if v != u and not visited[v]:
                        if relax(distances, d, v, 0):
                            queue.put((d, v, 0))

        visited[u] = True

    return None


runtests(spacetravel, all_tests=True)
