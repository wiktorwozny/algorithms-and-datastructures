G = {}

I = [(3, 4), (2, 5), (1, 3), (4, 6), (1, 4)]

for x, y in I:
    if x in G:
        G[x].append(y)
    else:
        G[x] = [y]

print(G)




