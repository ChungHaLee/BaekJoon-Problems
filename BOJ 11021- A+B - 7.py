# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
import sys
T = int(input())
test_cases = sys.stdin.readlines()

A = []
B = []

for i in test_cases:
    a, b = map(int, i.split())
    A.append(a)
    B.append(b)

for i in range(1, T+1):
    data = A[i-1] + B[i-1]
    print("Case #%d:" % i, data)

# 출력
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.