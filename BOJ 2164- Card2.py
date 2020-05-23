from collections import deque
n = int(input())
card = deque([i+1 for i in range(n)])

for _ in range(len(card)-1):
    del card[0]
    if len(card) > 1:
        card.append(card[0])
        del card[0]
print(card[0])