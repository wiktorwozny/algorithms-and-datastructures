from zad7testy import runtests


def hamiltonian(G, path, v, entry, visited):

    if len(path) == len(G):
        if path[-1] in G[0][1]:
            return True
        return False

    for u in G[v][entry % 2]:
        if not visited[u]:
            visited[u] = True
            path.append(u)
            if v in G[u][0]:
                if hamiltonian(G, path, u, 1, visited):
                    return True
            else:
                if hamiltonian(G, path, u, 2, visited):
                    return True

            visited[u] = False
            path.pop()

    return False


def droga(G):

    n = len(G)
    path = []
    visited = [False for _ in range(n)]

    path.append(0)
    visited[0] = True

    if hamiltonian(G, path, 0, 2, visited):
        return path

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)
