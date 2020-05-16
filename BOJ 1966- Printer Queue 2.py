# Printer Queue, 20-05-16, LeeChungHa
num = int(input())
import sys
n = []   # n = 문서의 수
m = []   # m = 궁금한 문서가 어느 위치인지
importance = []  # importance = n개 문서의 각 중요도
lst = sys.stdin.readlines()

for i in range(len(lst)):
    if i % 2 == 0:
        nk, mk = lst[i].split()
        n.append(int(nk))
        m.append(int(mk))
    else:
        lst[i] = lst[i].replace('\n', '')
        importance.append(lst[i])


rate = []

for j in range(num):
    im = importance[j].split()
    for i in im:
        rate.append(int(i))

data_lst = [[0 for _ in range(2)] for _ in range(n[j])]

for i in range(0, len(rate)):
    data_lst[i][0] += int(i)
    data_lst[i][1] += int(rate[i])

data_num = []

for i in range(len(data_lst)):
    data_num.append(data_lst[i][1])

# def first_data_priority(data_lst):
#     return data_lst[0][1]

def printing_queue(res_priority, data_lst):
    count = 0
    find_out(data_lst)

    for j in range(num):
        if res_priority == True:
            count += 1
            if m[j] == data_lst[0][0]:
                return count
        else:
            data_lst.append(rate[0])
            del rate[0]

        if len(data_lst) == 0:
            print(count)
        else:
            return printing_queue(res_priority, data_lst)


def find_out(data_lst):
    if data_lst[0][1] != max(data_num):
        res_priority = False
    else:
        res_priority = True

    return res_priority