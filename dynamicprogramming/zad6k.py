from zad6ktesty import runtests 

def haslo ( S ):

    n = len(S)
    DP = [-1 for i in range(n)]

    DP[0] = 1
    DP[1] = 2

    # for i in range(2, n):


runtests ( haslo )