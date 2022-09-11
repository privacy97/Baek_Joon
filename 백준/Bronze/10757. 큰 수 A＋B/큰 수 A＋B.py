A, B = map(str, input().split())

A = A[::-1]
B = B[::-1]

if len(A) < len(B):
    for i in range(len(B)-len(A)):
        A = A + '0'
else:
    for i in range(len(A)-len(B)):
        B = B + '0'

result = ''
up = 0

for i in range(len(A)):
    temp = up + int(A[i]) + int(B[i])
    
    if temp >= 10:
        t = temp-10
        result = str(t) + result
        up = 1
    else:
        result = str(temp) + result
        up = 0
        
if up == 1:
    result = '1' + result

print(result)