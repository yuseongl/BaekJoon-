N = int(input())
min = abs(N - (len(str(N))*9))

for i in range(min,N):
    each = sum(map(int,str(i)))
    if N == (i+each):
        print(i)
        break

else:
    print(0)