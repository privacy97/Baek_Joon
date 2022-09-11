def han_number(n):
    
    n = str(n)
    
    if len(n) == 1 or len(n) == 2:
        return True
    else:
        if int(n[0]) - int(n[1]) == int(n[1]) - int(n[2]):
            return True
        

n = int(input())

count = 0
for i in range(1,n+1):
    if han_number(i) == True:
        count = count + 1

print(count)
