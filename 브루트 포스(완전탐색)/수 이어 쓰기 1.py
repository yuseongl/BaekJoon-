N = int(input().rstrip())
answer = 0
leng = len(str(N))

for i in range(leng-1):
    answer += 9*10**i*(i+1)

print(answer+(N-10**(leng-1)+1)*leng)