n = int(input())

result = 0

for i in range(n):

    a = str(input())

    if len(a) == 1:
        result += 1

    a_list = [a[0]]

    for j in range(1, len(a)):
        if a[j-1] != a[j]:
            if a[j] in a_list:
                break
            else:
                a_list.append(a[j])
        else:
            a_list.append(a[j])
        
        if j == (len(a)-1):
            result += 1

print(result)
