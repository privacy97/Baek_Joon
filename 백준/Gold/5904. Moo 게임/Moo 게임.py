def moo(num, result):

    num += 1
    result = (result*2) + num

    if result >= n:
        return num, result

    return moo(num, result)


n = int(input())

if n < 26:
    if n == 1 or n == 4 or n == 8 or n == 11 or n == 16 or n == 19 or n == 23:
        print('m')
        exit()
    else:
        print('o')
        exit()

num = 3
result = 3

num, result = moo(num, result)

while True:

    n = n - num - int((result-num)/2)
    if n < 26:
        break

    num = 3
    result = 3

    num, result = moo(num, result)


if n == 1 or n == 4 or n == 8 or n == 11 or n == 16 or n == 19 or n == 23:
    print('m')
else:
    print('o')