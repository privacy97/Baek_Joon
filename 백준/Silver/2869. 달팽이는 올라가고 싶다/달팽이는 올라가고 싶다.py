import math

A, B, V = map(int, input().split())

n = (V-B)/(A-B)

print(math.ceil(n))