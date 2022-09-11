n = int(input())
a_list = []

for i in range(n):
    temp = str(input())
    a_list.append(temp)

for i in range(n):
    result = 0
    count = 0
    for j in a_list[i]:
        if j == 'X':
            count = 0
        else:
            count = count + 1
            result = result + count
    print(result)
        