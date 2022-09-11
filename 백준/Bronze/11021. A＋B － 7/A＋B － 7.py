n = int(input())

nlist = []

for i in range(n):
    a, b = map(int, input().split())
    nlist.append(a+b)

for i in range(n):
    print('Case #', end='')
    print(i+1, end='')
    print(':', nlist[i])