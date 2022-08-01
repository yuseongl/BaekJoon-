N = int(input().rstrip())
change = False
answer = 0
row = []
for i in range(N):
    row.append(list(input()))

for j in range(N):
    for k in range(N):
        try:
            if row[j][k] == row[j][k+1]:
                answer += 1
            elif (row[j][k] == row[j+1][k] or row[j][k] == row[j-1][k]) and change == False:
                answer += 1
                change = True
        except IndexError:
            pass