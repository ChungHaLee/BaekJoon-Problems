n = int(input())

import sys
data = sys.stdin.readlines()

for i in range(len(data)):
    data[i] = int(data[i])

stack = []
result = []
count = 1                    # count = 1부터 n까지 오름차순으로 스택에 쌓는 수

for _ in range(1, n+1):
    while count <= data[0]:  # 만들어야 하는 수열 맨 앞의 수가 될 때까지 count 를 스택에 쌓는다.
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data[0]:
        del data[0]
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result))



