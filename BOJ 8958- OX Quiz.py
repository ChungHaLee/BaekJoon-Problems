import sys
num = int(input())
test_case = sys.stdin.readlines()

for i in range(0, num):
    sum = 0
    count = 0
    for j in range(len(test_case[i])):
        if test_case[i][j] == 'O':
            sum += count + 1
            count += 1
        else:
            count = 0
    print(sum)