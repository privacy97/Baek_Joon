
a = str(input())

a = a.upper()

a_dic = {}

for i in a:
    if i in a_dic:
        a_dic[i] += 1
    else:
        a_dic[i] = 1

a_dic = sorted(a_dic.items(), key=lambda x:x[1], reverse=True)

if len(a_dic) == 1:
	print(a_dic[0][0])
elif (a_dic[0][1]) == (a_dic[1][1]):
    print('?')
else:
    print(a_dic[0][0])
