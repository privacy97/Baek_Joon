n = int(input())
n_list = list(map(int, input().split()))

n_max = max(n_list)

result = 0

for i in n_list:
    temp = i / n_max * 100
    result = result + temp
    
print(result/n)