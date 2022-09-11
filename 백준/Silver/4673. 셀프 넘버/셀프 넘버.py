def self_number(n):
    
    result = n
    
    for i in str(n):
        result = result + int(i)
        
    return result


a = list(range(1,10001))
b = list(range(1,10001))

for i in a:
    try:
    	b.remove(self_number(i))
    except:
        continue

for i in b:
    print(i)