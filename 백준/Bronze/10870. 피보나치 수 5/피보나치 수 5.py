n = int(input())

f_list = [0, 1]

count = 1

while count < n:
    f_list.append(f_list[len(f_list)-1]+f_list[len(f_list)-2])
    count += 1

print(f_list[n])