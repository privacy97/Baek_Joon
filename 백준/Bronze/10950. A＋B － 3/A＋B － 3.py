a = int(input())
lista = []

for i in range(a):
    temp = list(map(int, input().split()))
    lista.append(temp)
    
for i in range(a):
    print(lista[i][0]+lista[i][1])