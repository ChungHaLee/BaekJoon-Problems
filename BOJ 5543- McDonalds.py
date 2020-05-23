import sys
price = sys.stdin.readlines()
new_burger = []
new_soda = []

for i in range(0, 3):
    new_burger.append(int(price[i]))

for i in range(3, 5):
    new_soda.append(int(price[i]))

min_burger = min(new_burger)
min_soda = min(new_soda)

print(min_burger + min_soda - 50)