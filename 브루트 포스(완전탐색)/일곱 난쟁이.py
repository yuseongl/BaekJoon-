N = []
answer = 0
answer_list = []
visited = [False]*9
for i in range(9):
    N.append(int(input()))

for i in range(9):
    visited[i] = True
    for j in range(9):
        if visited[j] != True:
            visited[j] = True
            answer = 0
            answer_list = []
            for k in range(9):
                if visited[k] != True:
                    answer += N[k]
                    answer_list.append(N[k])
                if answer == 100 and len(answer_list) == 7:
                    answer_list.sort()
                    print(*answer_list,sep='\n')
                    break
            visited[j] = False
        if answer == 100 and len(answer_list) == 7:
            break
    visited[i] = False
    if answer == 100 and len(answer_list) == 7:
        break
