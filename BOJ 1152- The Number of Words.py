import sys
string = sys.stdin.readline()
count = 0
string = string.replace('\n', '')

for i in range(len(string)):
    if string[0] == ' ':
        pass
    if string[i] == ' ':
        count += 1

if string[0] != ' ':
    count += 1

if string[-1] == ' ':
    count -= 1


print(count)