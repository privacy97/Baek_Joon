a_list = []

for i in range(10):
    a = int(input())
    a = a % 42
    a_list.append(a)

a = set(a_list)

print(len(a))
