from collections import deque
from sys import stdin

T = int(input())

for i in range(T):
    p = stdin.readline().rstrip().replace('RR','')
    n = int(stdin.readline().rstrip())
    x = deque(stdin.readline().rstrip()[1:-1].split(','))
    R_cnt = 0
    if n == 0:
        x = []
    for j in p:
        if j == 'R':
            R_cnt += 1
        elif j == 'D':
            if len(x) == 0:
                print('error')
                break
            elif R_cnt%2 == 0:
                x.popleft()
            else:
                x.pop()
    else:
        if R_cnt%2 == 0:
            print('['+','.join(x)+']')
        elif R_cnt%2 != 0:
            x.reverse()
            print('['+','.join(x)+']')