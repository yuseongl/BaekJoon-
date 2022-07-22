from sys import stdin

N = int(stdin.readline().rstrip())
M = map(int,stdin.readline().split())

stack1 = list(M)
stack2 = []
answer = [-1 for i in range(N)]

for i in range(N-1):
    if stack1[i] >= stack1[i+1]:
        stack2.append(i)
    else:
        answer[i] = stack1[i + 1]
        for j in range(N):
            if len(stack2) != 0 and stack1[stack2[-1]] < stack1[i+1]:
                answer[stack2[-1]] = stack1[i+1]
                stack2.pop()
            else:
                break
print(*answer)