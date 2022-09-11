test = int(input())

for i in range(test):
    H, W, N = map(int, input().split())
    
    temp = N % H
    if temp == 0:
        temp = H
    
    print(temp, end='')
    
    temp = (N//H)+1
    
    if N % H == 0:
        temp -= 1
    
    
    if temp < 10:
        print('0', end='')
        print(temp)
    else:
        print(temp)
    