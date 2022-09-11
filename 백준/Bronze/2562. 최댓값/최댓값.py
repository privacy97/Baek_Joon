a_list = []

for i in range(9):
    a = int(input())
    a_list.append(a)

temp = max(a_list)

print(temp)
print(a_list.index(temp)+1)