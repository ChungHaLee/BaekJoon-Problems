import sys
data = sys.stdin.readlines()

for i in range(len(data)):
    data[i] = int(data[i])

ans = []

for i in data:
    ans.append(i % 42)


lst = []
for i in range(len(ans)):
    if ans[i] not in ans[i+1:]:
        lst.append(ans[i])
print(len(lst))