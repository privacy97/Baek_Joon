import bisect

def prime_list(n):
    
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


n = int(input())

for i in range(n):
    A = int(input())

    x = prime_list(A+1)

    #print(x)

    if int(A/2) in x:
        print(int(A/2), int(A/2))
    else:
        x_right = bisect.bisect_left(x, int(A/2))
        x_left = x_right - 1
        
        while True:
            if x[x_left] + x[x_right] == A:
                print(x[x_left], x[x_right])
                break
            
            elif x[x_left] + x[x_right] > A:
                x_left -= 1
                
            elif x[x_left] + x[x_right] < A:
                x_right += 1