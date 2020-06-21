for x in range(1, 10):
    if x % 3 == 0:
        break
    print(x, end= " ")  # break 문 때문에 x = 3 일 때 for 문 (반복문)이 종료된다.
print("끝")