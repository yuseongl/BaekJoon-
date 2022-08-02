from collections import deque

N, M = map(int,input().split())
visited = [False]*N
num = range(1,N+1)
list_ = []

def seq(num,visited,M):
    deq = deque(range(1, N + 1))
    if M != 0:
        for i in num:
            v = deq.popleft()
            print(list(deq))
            if visited[i-1] == False:
                visited[i-1] = True
                list_.append([i,v])
                seq(num,visited,M-1)
                visited[i-1] = False

seq(num,visited,M)

print(list_)