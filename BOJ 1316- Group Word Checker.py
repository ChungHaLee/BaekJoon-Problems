import sys
num = int(input())
word = sys.stdin.readlines()
lst = []
cnt = 0

for i in range(len(word)):
    word[i] = word[i].replace('\n', '')


def is_all_unique(lst):
    for m in range(len(lst)):
        if len(set(lst)) == len(lst):
            return True


def is_all_same(lst):
    for m in range(len(lst)):
        if len(set(lst)) == 1:
            return True


def define_unique(lst):
    for m in range(len(lst)-2):
        if lst[m+1] != lst[m] and lst[m] in lst[m+2:]:
            return False
    return True

for i in range(num):
    for j in range(len(word[i])):
        lst.append(word[i][j])
    if is_all_unique(lst) == True or is_all_same(lst) == True or define_unique(lst) != False or len(lst) == 1:
        cnt += 1
    lst = []

print(cnt)


