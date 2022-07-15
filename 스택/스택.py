from sys import stdin
stack = []
cnt = 1
def push(i):
    stack.append(i)
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())
def size():
    print(len(stack))
def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
for i in range(10000):
    N = stdin.readline().rstrip()
    if 'push' in N:
        a,b = N.split()
        push(b)
    elif N == 'pop':
        pop()
    elif N == 'size':
        size()
    elif N == 'empty':
        empty()
    elif N == 'top':
        top()
    else:
        cnt = int(N)
    if i == cnt:
        break

