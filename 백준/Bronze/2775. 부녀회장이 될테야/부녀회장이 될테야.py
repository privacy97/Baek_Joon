n_list = [list(range(1,15))]

#print(n_list)

for i in range(14):
    temp = [1]
    for j in range(13):
        temp.append(n_list[i][j+1]+temp[j])
    n_list.append(temp)
    #print(temp)

test_case = int(input())

for i in range(test_case):
    k = int(input())
    n = int(input())

    print(n_list[k][n-1])