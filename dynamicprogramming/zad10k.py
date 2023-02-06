from zad10ktesty import runtests


def f(n, DP):

    if DP[n] != 0:
        return DP[n]

    if n == 0:
        return 0

    min_val = 10**100
    x = 1
    while x * x <= n:
        if x * x == n:
            DP[n] = 1
            return DP[n]

        min_val = min(min_val, f(n - x * x, DP) + 1)
        x += 1

    DP[n] = min_val
    return DP[n]


def dywany(N):

    DP = [0 for _ in range(N + 1)]

    f(N, DP)
    print(DP[N])
    # print(DP)
    ans = []
    i = N
    while i > 0:
        j = 1
        while i - j*j >= 0:
            if DP[i - j * j] == DP[i] - 1:
                break
            j += 1
        ans.append(j)
        i -= j * j

    ans.sort()

    return ans


runtests( dywany )

