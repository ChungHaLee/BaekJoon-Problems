import sys
C = int(input())
data = sys.stdin.readlines()
student = []
scores_list = []

for i in data:
    s_data = i.split()
    student.append(int(s_data[0]))
    scores_list.append(s_data[1:])

sum_lst = []
average = []

for i in range(len(scores_list)):
    sum = 0
    for j in range(len(scores_list[i])):
        sum += int(scores_list[i][j])
    sum_lst.append(sum)

for i in range(len(student)):
    average.append(sum_lst[i]/student[i])

for i in range(len(scores_list)):
    for j in range(len(scores_list[i])):
        scores_list[i][j] = int(scores_list[i][j])

for i in range(len(scores_list)):
    count = 0
    for k in range(len(scores_list[i])):
        if scores_list[i][k] > average[i]:
            count += 1
    ans = count / len(scores_list[i]) * 100
    print("%.3f%%" % ans)