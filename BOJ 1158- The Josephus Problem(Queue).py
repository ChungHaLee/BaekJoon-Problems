n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

ans = []
cnt = 0

for i in range(n):
    cnt += k-1  # cnt 인덱스를 범위 3만큼 계속 늘려간다
    if cnt >= len(arr):
        cnt = cnt % len(arr)
    ans.append(str(arr.pop(cnt)))

print('<', ', ' .join(ans)[:],'>', sep='')