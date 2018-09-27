# Backjoon Online Judge No.3036
# Python

from math import gcd

N = int(input())
rings = list(map(int, input().split()))

for i in range(1, N):
    d = gcd(rings[0], rings[i])
    print(str(rings[0]//d) + '/' + str(rings[i]//d))