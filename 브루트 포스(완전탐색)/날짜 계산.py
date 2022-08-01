N = list(map(int,input().split()))
years = 0
E = 0
S = 0
M = 0
while True:
    years += 1
    E += 1
    S += 1
    M += 1
    if E%15 == 1:
        E = 1
    if S%28 == 1:
        S = 1
    if M%19 == 1:
        M = 1
    if E == N[0] and S == N[1] and M == N[2]:
        print(years)
        break