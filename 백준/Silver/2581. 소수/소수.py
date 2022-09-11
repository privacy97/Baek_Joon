def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
  
A = int(input())
B = int(input())

n_list = list(range(A, B+1))

prime_list = []

for i in n_list:
    if prime(i) == True:
        prime_list.append(i)

if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])