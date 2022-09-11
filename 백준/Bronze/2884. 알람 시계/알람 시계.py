temp = list(map(int, input().split()))

if temp[1] < 45:
    temp[1] = temp[1]+15
    if temp[0] == 0:
        temp[0] = 23
    else:
        temp[0] -= 1
else:
    temp[1] -= 45
    
print(temp[0], temp[1])