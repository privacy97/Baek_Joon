n = int(input())

for i in range(n):
    temp = list(map(int, input().split()))
    del temp[0]
    
    aver = sum(temp)/len(temp)
    
    count = 0
    for j in temp:
        if aver < j:
            count = count + 1
    
    temp = count/len(temp)*100
    print(f'{temp:.3f}%')