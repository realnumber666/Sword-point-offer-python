from collections import deque
d = deque(["abc"])
d.append(1)
d.appendleft(2)
print d.pop()
print d.popleft()


print d