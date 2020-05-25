n, m = map(int, input().split())
tree_height = list(map(int, input().split()))

def treesum(height):                  # sum 함수를 따로 뺀 이유 ?
    sum = 0
    for i in tree_height:
        if i-height > 0:              # 나무의 높이가 톱날의 높이보다 높은 경우에만 나무를 가져갈 수 있다(줄자 같은 개념)
            sum += i-height
    return sum                        # sum = 얻을 수 있는 나무의 합

def binary_search(target):            # target = 적어도 필요한 나무의 길이
    start, end = 1, max(tree_height)  # start, end = 톱의 높이 범위 시작값과 끝 값
    saw = 0                           # saw = 톱의 높이
    while start <= end:              # start 와 end 가 같을 때까지 시행
        mid = (start + end) // 2      # mid = 톱의 높이 중간값(bs 할 것이므로 중간값 필요^^)
        sum = treesum(mid)            # sum = 톱의 높이가 중간값일 때 얻을 수 있는 나무의 합
        if sum < target:              # 그 때 나무의 합이 target 보다 작을 때
            end = mid - 1             # 끝 값을 하나 더 내린다 - 톱의 높이 낮추기
        if sum >= target:             # 그 때 나무의 합이 target 보다 같거나 클 때
            saw = mid                 # 이 때 톱의 높이의 최솟값 = mid
            start = mid + 1           # 시작값을 하나 더 올린다 - 톱의 높이 올리기
    return saw

print(binary_search(m))
