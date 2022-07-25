from collections import deque

N,K = map(int,input().split())
que = deque(range(N,0,-1))
answer = []
while len(que) != 0:
    for i in range(K):
        que.appendleft(que.pop())
    answer.append(que.popleft())
print('<%s>'%', '.join(map(str,answer)).strip())