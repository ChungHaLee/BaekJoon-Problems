# 입력
# 첫 째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다.
# 주어지는 자연수는 100 보다 작다.
import sys
numbers = sys.stdin.readlines()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

maxi = max(numbers)
index = numbers.index(maxi)+1
print(maxi, index, sep='\n')

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.