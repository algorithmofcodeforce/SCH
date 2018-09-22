# Backjoon Online Judge No.1094
# Python


Stick, cnt = 0, 0
i = 6

X = int(input())

# 모든 Xcm은 서로 다른 막대 사이즈로 만들어진다.
while(True):
    if Stick + (2 ** i) > X:
        i -= 1

    elif Stick == X:
        break

    else:
        Stick += (2 ** i)
        cnt += 1
        i -= 1

print(cnt)
