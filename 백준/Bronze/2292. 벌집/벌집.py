n = int(input())

bee_house = 1

count = 1

while n > bee_house:
    bee_house += 6 * count
    count += 1

print(count)