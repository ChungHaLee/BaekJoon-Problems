import sys
data = map(int, sys.stdin.readline().split())

h, m = data

if h != 0 and m >= 45:
    print(h, m-45)
elif h != 0 and m < 45:
    print(h-1, m+60-45)
elif h == 0 and m >= 45:
    print(h, m-45)
elif h == 0 and m < 45:
    print(23, m+60-45)
# 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다.