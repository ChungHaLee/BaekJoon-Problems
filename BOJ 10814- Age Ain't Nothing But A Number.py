n = int(input())

import sys
data = sys.stdin.readlines()

data_lst = []

for idx, line in enumerate(data): # enumerate 함수의 기능
    age, name = line.split()
    age = int(age)
    data_lst.append([age, name, idx])

sorted_data_lst = sorted(data_lst, key=lambda x: x[2])
real_sorted_data_lst = sorted(sorted_data_lst, key=lambda x: x[0])

for line in real_sorted_data_lst:
    age, name, idx = line # 리스트 언패킹
    print(age, name)