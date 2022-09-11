n = str(input())
result = ''
count = 0

temp = ''

for i in n:
    if i == '-' and count == 0:
        temp = int(temp)
        result += str(temp)
        temp = ''

        result += str(i)
        result +='('
        count = 1

    elif i == '-' and count == 1:
        temp = int(temp)
        result += str(temp)
        temp = ''

        result +=')'
        result += str(i)
        result +='('
        count = 1

    elif i == '+':
        temp = int(temp)
        result += str(temp)
        temp = ''
        result += str(i)
        
    else:
        temp += str(i)

if temp != '':
    temp = int(temp)
    result += str(temp)
    temp = ''


if count == 1:
    result += ')'

#print(result)

result = eval(result)

print(result)