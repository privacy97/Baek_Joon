n = int(input())

count = 2
    
while True:
    if n%count == 0:
        print(count)
        n = int(n/count)
    else:
        count += 1
    
    if n == 1:
        break