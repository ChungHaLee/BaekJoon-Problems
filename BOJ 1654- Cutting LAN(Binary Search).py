import sys
k, n = map(int, input().split())
k_length = list(map(int, sys.stdin.readlines()))

def lans_sum(final):                  # final = 최소값과 최대값의 평균
    sum = 0
    for leng in k_length:
        sum += int(leng//final)
    return sum                        # sum = '각' 랜선을 중간값 medium 으로 나눈 것의 '합'

def binary_search(n):
    start, end = 1, max(k_length)     # 랜선 자르기이므로 최소 1cm는 잘라야 함, start 최소값, end 최대값
    lans = 0                          # lans = n개로 자를 수 있는 랜선 길이의 최대값
    while start <= end:
        medium = int((start+end)//2)  # medium = 최소값과 최대값의 평균(중간값)
        sum = lans_sum(medium)
        if sum < n:
            end = medium - 1
        if sum >= n:
            lans = medium
            start = medium + 1
    return lans

print(binary_search(n))







