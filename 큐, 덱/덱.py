from collections import deque
from sys import stdin

N = int(stdin.readline().rstrip())
deq = deque()
for i in range(N):
    M = stdin.readline().rstrip()
    if 'push_back' in M:
        a,b = M.split()
        deq.appendleft(b)
    elif 'push_front' in M:
        a, b = M.split()
        deq.append(b)
    elif M == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif M == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif M == 'size':
        print(len(deq))
    elif M == 'empty':
        if len(deq) != 0:
            print(0)
        else:
            print(1)
    elif M == 'front':
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)
    elif M == 'back':
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)