# Backjoon Online Judge No.1547
# Python


def swap(x, y):
    tmp = cups[x]
    cups[x] = cups[y]
    cups[y] = tmp

cups = [-1, 1, 0, 0]

M = int(input())
for i in range(M):
    X, Y = map(int, input().split())
    swap(X, Y)

try:
    print(cups.index(1))
except:
    print(cups[0])
