# Backjoon Online Judge No.2609
# Python

from math import gcd

A, B = map(int, input().split())

print(gcd(A, B))
print(A * B // gcd(A, B))
