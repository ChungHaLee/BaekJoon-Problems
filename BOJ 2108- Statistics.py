import sys
from collections import Counter

num = int(sys.stdin.readline())

numbers = []

for _ in range(num):
    numbers.append(int(sys.stdin.readline()))

numbers = sorted(numbers)



def mean(new_num):
    return round(sum(new_num)/len(new_num))


def middle(new_num):
    mid = new_num[len(new_num)//2]  # 반으로 나눈 몫 구하기
    return mid


def the_most_num(new_num):
    new_num = Counter(new_num)
    modes = new_num.most_common()
    if len(modes) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]
    return mod


def the_range(new_num):
    if len(new_num) != 1:
        if new_num[0] < new_num[-1]:
            ranges = abs(new_num[-1] - new_num[0])
        else:
            ranges = abs(new_num[-1] + new_num[0])
    else:
        ranges = 0
    return ranges


#1. 산술평균
print(mean(numbers))

#2. 중앙값
print(middle(numbers))

#3. 최빈값
print(the_most_num(numbers))

#4. 범위
print(the_range(numbers))