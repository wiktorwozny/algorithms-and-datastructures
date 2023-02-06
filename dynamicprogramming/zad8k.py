from zad8ktesty import runtests 


def napraw(s, t):

    S = len(s)
    T = len(t)

    DP = [[-1 for i in range(S)] for j in range(T)]

    for i in range(S):
        if i == 0:
            if s[i] == t[0]:
                DP[0][i] = 0
            else:
                DP[0][i] = 1
        else:
            if s[i] != t[0]:
                DP[0][i] = DP[0][i - 1] + 1
            else:
                DP[0][i] = i

    for i in range(T):
        if i == 0:
            if s[0] == t[i]:
                DP[i][0] = 0
            else:
                DP[i][0] = 1
        else:
            if s[0] != t[i]:
                DP[i][0] = DP[i - 1][0] + 1
            else:
                DP[i][0] = i

    # for i in range(T):
    #     print(DP[i])

    for a in range(1, T):
        for b in range(1, S):
            if t[a] == s[b]:
                DP[a][b] = DP[a - 1][b - 1]
            else:
                DP[a][b] = min(DP[a - 1][b], DP[a - 1][b - 1], DP[a][b - 1]) + 1

    return DP[T - 1][S - 1]


runtests(napraw)