# Backjoon Online Judge No.1934
# Python


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    lcm = A * B // gcd(A, B)
    print(lcm)
