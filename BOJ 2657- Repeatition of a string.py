import sys
data = sys.stdin.readlines()
num_lst = []
case_lst = []

for i in data:
    num_lst.append(int(i[0]))
    case_lst.append(i[2:])

for i in range(len(case_lst)):  # case_lst[i]에서 개행 문자 없앤 뒤 다시 저장하기 (다시 저장 꼭 하기)
    case_lst[i] = case_lst[i].replace('\n', '')


for i in range(len(case_lst)):
    for m in range(len(case_lst[i])):
        print(case_lst[i][m] * num_lst[i], end='')
    if case_lst[i] == '':
        pass
    else:
        print()