import sys
n = sys.stdin.readline()
n = n.replace('\n', '')

count = 1
real_num = n
next_num = ''


while next_num != real_num:
    if int(n) < 10:
        n = '0' + n
    temp = str(n[-1])
    sep = int(n[0]) + int(n[-1])
    sep = str(sep)
    next_num = temp + sep[-1]
    n = next_num

    if int(n) != int(real_num):
        count += 1
    else:
        print(count)
        break  # break 구문의 활용



# 0: 1
# 1: 60
# 2: 20
# 3: 60
# 4: 20
# 5: 3
# 6: 20
# 7: 60
# 8: 20
# 9: 60