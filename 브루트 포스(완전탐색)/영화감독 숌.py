import sys
sys.setrecursionlimit(10**6)
num = 666
N = int(input())

def DFS(num):
    if '666' in str(num):
        return num+1
    return DFS(num+1)

for i in range(N):
    num = DFS(num)

print(num-1)
