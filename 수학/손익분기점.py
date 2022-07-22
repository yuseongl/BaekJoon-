A,B,C = map(float,input().split())
if C-B > 0:
    print(int(A/(C-B))+1)
else:
    print(-1)