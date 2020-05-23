import sys
numbers = sys.stdin.readline().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers = sorted(numbers)
print(numbers[1])