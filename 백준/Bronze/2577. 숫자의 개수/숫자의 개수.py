A = int(input())
B = int(input())
C = int(input())

n = A*B*C

n = str(n)
n_list = []

for i in range(len(n)):
    n_list.append(n[i])

for i in range(10):
    print(n_list.count(str(i)))