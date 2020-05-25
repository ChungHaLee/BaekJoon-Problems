from collections import defaultdict
dict = defaultdict(lambda: 0)

n = int(input())
for i in list(map(int, input().split())):
    dict[i] += 1

m = int(input())
for i in list(map(int, input().split())):
    if i in dict:
        print(dict[i], end= ' ')
    else:
        print(0, end = ' ')