test_case = int(input())

for i in range(test_case):
    list_a = list(map(str, input().split()))
    
    for j in list_a[1]:
        for k in range(int(list_a[0])):
            print(j, end='')
    print()