# Backjoon Online Judge No.1934
# Python

floor = [list(range(15))]


def cal_floor():
    for f in range(1, 15):
        floor.append([0])
        for r in range(1, 15):
            floor[f].append(floor[f-1][r]+floor[f][r-1])


cal_floor()

num = int(input())

for i in range(num):
    f = int(input())
    r = int(input())
    print(floor[f][r])