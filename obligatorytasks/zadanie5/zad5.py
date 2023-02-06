from queue import PriorityQueue
from zad5testy import runtests


def plan(T):

    A = [[0, 0] for _ in range(len(T))]
    for i in range(len(T)):
        A[i][0] = T[i]
        A[i][1] = i

    queue = PriorityQueue()

    e = T[0]
    currenti = 0
    ans = [0]

    while currenti + e < len(T) - 1:
        maxi = currenti + e
        for i in range(currenti + 1, maxi + 1):
            if T[i] != 0:
                to_put = [A[i][0] * (-1), A[i][1]]
                queue.put(to_put)

        e, tmp = queue.get()
        e *= (-1)
        ans.append(tmp)
        currenti = maxi

    ans.sort()

    return ans


runtests( plan, all_tests = True )