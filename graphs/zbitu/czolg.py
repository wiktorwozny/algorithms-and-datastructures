'''
Pewien podróżnik chce przebyć trasę z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.
'''

from queue import PriorityQueue as PQ
from math import inf

# startujemy z v, konczymy na s, mamy pojemnosc D, graf G, T to tablica cen za litr paliwa


def tank(G, a, b, D, T):

    n = len(G)
    prices = [[inf for _ in range(D)] for _ in range(n)]
    visited = [[False for _ in range(D)] for _ in range(n)]
    queue = PQ()

    queue.put((0, a, 0))  # dotychczasowe wyjebane siano, wierzcholek, palwko które zostało es
    visited[0][0] = True
    prices[0][0] = 0

    while not queue.empty():
        x, u, l = queue.get()

        if u == b:
            return x

        if not visited[u][l]:
            visited[u][l] = True
            i = 0
            while i + l <= D:
                for v, d in G[i]:
                    if l + i - d >= 0 and prices[v][l + i - d] > x + i * T[u]:
                        prices[v][l + i - d] = x + i * T[u]
                        queue.put((x + i * T[u], v, l + i - d))

                i += 1

    return None
