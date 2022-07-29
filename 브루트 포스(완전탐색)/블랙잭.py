N,M = map(int,input().split())
num_list = list(map(int,input().split()))

visited = [False]*N
num = 0
num2 = 0
cnt = 0

for j in range(N):
    visited[j] = True
    for k in range(N):
        if visited[k] == True:
            break
        visited[k] = True
        for m in range(N):
            if visited[m] == True:
                break
            elif num_list[j]+num_list[k]+num_list[m] == M:
                num = num_list[j]+num_list[k]+num_list[m]
                print(num)
                cnt = 1
                break
            else:
                num = num_list[j]+num_list[k]+num_list[m]
                if M > num > num2:
                    num2 = num
        visited[k] = False
        if num == M:
            break
    visited[j] = False
    if num == M:
        break
if cnt == 0:
    print(num2)