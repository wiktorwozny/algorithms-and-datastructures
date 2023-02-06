'''
Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada
mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P. Pełnego baku wystarczy na przejechanie
odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
odległość d bez tankowania).
'''

from math import inf
from queue import PriorityQueue
# TO KOMENTARZE Z TAMETGO ROKU WIEC SA RACZEJ DO DUPY NAPISANE BO PISALAM JE DO SB XD

# wrzucam do kolejki krotki (dystans, wierzchołek, ilosc paliwa z ktorym wyruszamy)
# tworze distance ktory dla kazdego wierzcholka ma tablice dlugosci d, pod kazdym indeksem jest zapisana dlugosc najkrotszej trasy takiej ze dojedzamy z inx paliwa do wietrzchołka

# szukanie rozwiania niestety jest trudne, robie tak samo tablice parentow dla kazdego wierzcholka z d miejscami,
# gdzie zapisuje parenta konkretnego jako krotke (wierzcholek i z jaka iloscia z tego wierzcholka wyruszl), jezeli
# wyruszyl z ilosc d to znaczy ze tam tankowal
# przez co musze znalezc indeks pod ktorym ma dotychasz zapisana najkrotsza trase i z tego miejsca kontynuuje
def jak_dojade(G, P, d, a ,b):
    n = len(G)
    distance = [[inf] * d for _ in range(n)]
    for i in range(d):
        distance[a][i] = 0
    K = PriorityQueue()

    K.put((0, a, d))
    #visited = [False for _ in range(n)]
    p = [[-1]*d for _ in range(n)]

    while not K.empty():
        u = K.get()

        if u[1] == b:
            path = [b]
            parent = p[b][u[2]]
            while parent[0] != a:
                path.append(parent[0])
                if parent[1] == d:
                    max = 0
                    for i in range(d):
                        if distance[parent[0]][i] < distance[parent[0]][max]:
                            max = i
                    parent = p[parent[0]][max]
                else:
                    parent = p[parent[0]][parent[1]]

            path.append(a)
            return path[::-1]

        for x in range(n):
            if G[u[1]][x] > 0 and G[u[1]][x] <= u[2]:
                if distance[x][u[2] - G[u[1]][x]] > G[u[1]][x] + u[0]:
                    distance[x][u[2] - G[u[1]][x]] = G[u[1]][x] + u[0]
                    p[x][u[2] - G[u[1]][x]] = (u[1],u[2])
                    if x in P:
                        K.put((distance[x][u[2]-G[u[1]][x]], x, d))
                    else:
                        K.put((distance[x][u[2]-G[u[1]][x]], x, u[2] - G[u[1]][x]))

    return None





G = [[-1, 6,-1, 5, 2],
     [-1,-1, 1, 2,-1],
     [-1,-1,-1,-1,-1],
     [-1,-1, 4,-1,-1],
     [-1,-1, 8,-1,-1]]
P = [0,1,3]

print(jak_dojade(G, P, 6, 0, 2))
'''print(k)
print(l)'''