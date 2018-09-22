# Backjoon Online Judge No.13241
# Python

# 범위가 늘어났지만 Python은 강력했다.
# 1934의 알고리즘을 그대로 이용하였다.

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

A, B = map(int, input().split())

lcm = A * B // gcd(A, B)

print(lcm)