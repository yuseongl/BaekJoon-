N = str(input())
if int(N) < 10:
    answer = '0' + N
else:
    answer = N
cnt = 0
while True:
    num_ad = 0  # 두 수 더하기
    num_str = 0
    if 3 > len(N) > 1:    # 두 자리 원 사이클
        num_ad = int(N[0]) + int(N[1])
        if num_ad > 9:
            num_ad_str = str(num_ad)
            num_str = N[1] + num_ad_str[1]
            if num_str == answer:
                cnt += 1
                print(cnt)
                break
            else:
                N = num_str
                cnt += 1
        else:
            num_str = N[1] + str(num_ad)
            if num_str == answer:
                cnt += 1
                print(cnt)
                break
            else:
                N = num_str
                cnt += 1
    elif len(N) == 1: # 한 자리 원사이클
        N = '0'+ N
    else:
        break