n = int(input())

number = 1
count = 1

while number < n:
    count += 1
    number += count

#print(count)
#print(number)
#print(n)

if (count%2==1):
    print((1+(number-n)), end='/')
    print((count-(number-n)))
    
else:
    print((count-(number-n)), end='/')
    print((1+(number-n)))