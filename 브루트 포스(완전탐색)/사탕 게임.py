N = int(input().rstrip())
change = False
answer_row = 0
answer = 0
store_row = 0
row = []
for i in range(N):
    row.append(list(input()))

for j in range(N):
    change = False
    answer_row = 0
    store_row = row[j][0]
    for k in range(N):
        if store_row == row[j][k]:
            answer_row += 1
        elif store_row != row[j][k]:
            try:
                if j==0 and store_row == row[j+1][k] and change == False:
                    change = True
                    answer_row += 1
                elif j==N-1 and store_row == row[j-1][k] and change == False:
                    change = True
                    answer_row += 1
                elif (store_row == row[j+1][k] or store_row == row[j-1][k]) and change == False:
                    if j-1 != -1:
                        change = True
                        answer_row += 1
                elif store_row == row[j][k+1]:
                    change = True
                    answer_row += 1
                    store_row = row[j][k]

                else:
                    change = False
                    store_row = row[j][k]
                    if answer < answer_row:
                        answer = answer_row
                    answer_row = 1
            except IndexError:
                pass
    if answer < answer_row:
        answer = answer_row

for j in range(N):
    change = False
    answer_row = 0
    store_row = row[0][j]
    for k in range(N):
        if store_row == row[k][j]:
            answer_row += 1
        elif store_row != row[k][j]:
            try:
                if j==0 and store_row == row[k][j+1] and change == False:
                    change = True
                    answer_row += 1
                elif j==N-1 and store_row == row[k][j-1] and change == False:
                    change = True
                    answer_row += 1
                elif (store_row == row[k][j+1] or store_row == row[k][j-1]) and change == False:
                    if j-1 != -1:
                        change = True
                        answer_row += 1
                elif store_row == row[k+1][j]:
                    change = True
                    answer_row += 1
                    store_row = row[k][j]
                else:
                    change = False
                    store_row = row[k][j]
                    if answer < answer_row:
                        answer = answer_row
                    answer_row = 1
            except IndexError:
                pass
    if answer < answer_row:
        answer = answer_row

print(answer)