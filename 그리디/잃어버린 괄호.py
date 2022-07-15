N = input()
a = str()
choi = str()
b = 0
c = 0
cnt = 0
for i in N:
    if (i == '-' or i == '+') and cnt == 0:
        if i == '-':
            choi = '-'
            cnt += 1
        b += int(a)
        a = str()
    elif i == '+' or i == '-':
        c += int(a)
        a = str()
    else:
        a += i
if choi == '-':
    print(b-(c+int(a)))
else:
    print(b+c+int(a))