N = int(input())
M = []
rank = []
num = 0

for i in range(N):
    M.append(list(map(int,input().split())))

def DFS(a,b,n,c):
    if n == N:
        return rank.append(c)
    elif a < M[n][0] and b < M[n][1]:
        c += 1
    DFS(a,b,n+1,c)

for i,j in M:
    cnt = 1
    DFS(i,j,num,cnt)

print(*rank)