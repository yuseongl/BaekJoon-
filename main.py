from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
stack1 = deque()  # 숫자열 받는 스택
stack2 = deque()  # 늘어놓는 스택
diff = deque()  # 입력숫자 받는 스택
answer = deque()  # +-받는 스택
i = 1

def push(i,M):
    if i > M:
        return i
    stack1.append(i)
    answer.append('+\n')
    if i == M:
        return i+1
    return push(i+1,M)

def pop():
    if len(stack1) != 0:
        stack2.append(stack1.pop())
        answer.append('-\n')

for j in range(1,N+1):
    M = int(stdin.readline().rstrip())
    diff.append(M)
    i = push(i,M)
    if M == stack1[-1]:
        pop()
        if len(diff) == N:
            print(''.join(answer))
    elif M < stack2[-1]:
        print('NO')
        break