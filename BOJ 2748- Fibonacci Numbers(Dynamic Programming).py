# 피보나치수 동적프로그래밍으로 만들기 (재귀용법 x)
n = int(input())

def fibo(n):
    cache = [0 for i in range(n+1)]
    cache[0] = 0   # 메모이제이션 기법
    cache[1] = 1
    for i in range(2, n+1):
        cache[i] = cache[i-2] + cache[i-1]
    return cache[n]

print(fibo(n))