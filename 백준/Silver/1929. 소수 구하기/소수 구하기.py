def prime_list(n):
    
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

A, B = map(int, input().split())

x = prime_list(B+1)

for i in x:
    if i >= A:
        print(i)