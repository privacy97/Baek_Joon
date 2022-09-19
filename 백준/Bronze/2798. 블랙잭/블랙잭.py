from itertools import combinations

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
find = float("inf")


for i in combinations(n_list, 3):
    temp = m - (i[0] + i[1] + i[2])

    if temp >= 0 and temp < find:
        result = (i[0] + i[1] + i[2])
        find = temp

print(result)