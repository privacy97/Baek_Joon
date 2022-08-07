a, b, c = map(int, input().split())

count = 1

if b >= c:
    print(-1)
    exit()

print(int(a/(c-b)+1))