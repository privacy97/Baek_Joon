def prime_list(n):
    
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

while True:
    B = int(input())
    if B == 0:
        break

    x = prime_list(int(B*2)+1)
    y = prime_list(B+1)

    print(len(x)-len(y))