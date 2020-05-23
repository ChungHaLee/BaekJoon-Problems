import sys
command = sys.stdin.readlines()
from collections import deque
queue = deque()

for i in range(1, len(command)):
    if 'push' in command[i]:
        command[i] = command[i].replace('push', '')
        command[i] = command[i].strip()
        queue.append(command[i])
    if 'pop' in command[i]:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    if 'size' in command[i]:
        print(len(queue))
    if 'empty' in command[i]:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if 'front' in command[i]:
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    if 'back' in command[i]:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)