dic = {'c=' : 1, 'c-' : 1,'dz=' : 1,'d-' : 1,'lj' : 1,'nj' : 1, 's=' : 1,'z=' : 1}

a = str(input())

result = 0

while True:
    if len(a) == 0:
        break
    try:
        try:
            result += dic[a[0:2]]
            a = a[2:]
        except:
            result += dic[a[0:3]]
            a = a[3:]
    except:
        result += 1
        a = a[1:]

print(result)