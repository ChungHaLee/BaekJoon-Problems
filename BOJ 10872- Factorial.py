num = int(input())

def multiply(n):
    if n <= 1:
        return 1
    return n * multiply(n-1)

print(multiply(num))