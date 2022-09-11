n = int(input())

five = n//5

for i in reversed(range(five+1)):
    temp = n - (5*i)
    
    if temp%3 == 0:
        print(i+(temp//3))
        exit()
    elif i == 0:
        print(-1)