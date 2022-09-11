def prime(n):
    if n == 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1
  

n = int(input())
n_list = list(map(int, input().split()))

count = 0

for i in n_list:
    count += prime(i)

print(count)