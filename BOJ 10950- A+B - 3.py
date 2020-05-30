# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
import sys
T = int(input())
test_cases = sys.stdin.readlines()

A = []
B = []

for i in test_cases:
    a, b = map(int, i.split())
    A.append(a)
    B.append(b)

for i in range(T):
    data = A[i] + B[i]
    print(data)

