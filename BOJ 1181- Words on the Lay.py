# 첫째 줄에 단어의 개수 N이 주어진다. (1≤N≤20,000)
# 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
# 길이가 짧은 것부터 / 길이가 같으면 사전 순으로

# sorted 에는 람다식을 활용해 여러 조건을 줄 수 있다.
# key 와 lambda 함수를 이용해 여러 가지 조건을 줄 수 있다.
# 동시에 두 가지 기준을 줄 수도 있다 (첫번째 기준 , 두번째 기준)
# 첫번째 기준으로 정렬이 되지 않으면, 두번째 기준을 적용하여 정렬한다

import sys
n = int(input())
words = sys.stdin.readlines()
lst = [str(w) for w in words]
lst = set(lst)
lst = sorted(lst)

new_lst = sorted(lst, key=lambda x: len(x))
a = ''

for i in range(len(new_lst)):
    a += new_lst[i]
print(a)