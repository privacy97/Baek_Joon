time = list(map(int, input().split()))
timer = int(input())

time[0] = time[0] + int(timer/60)
time[1] = time[1] + int(timer%60)

if time[1] >= 60:
    time[1] -= 60
    time[0] += 1

while True:
    if time[0] < 24:
        break
    time[0] -= 24

print(time[0], time[1])