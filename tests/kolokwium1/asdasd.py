from collections import deque

q = deque()

q.append(2)
q.append(1)
q.append(4)

print(q)
asd = q.popleft()
print(asd)
print(len(q))
print(q)