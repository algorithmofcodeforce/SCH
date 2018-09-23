# Backjoon Online Judge No.10253
# Python


# 분수 계산을 위해 Fraction을 이용한다.
from fractions import Fraction


T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    X = Fraction(a, b)

    tmp = 1
    # 마지막 분모를 찾는 과정에서 시간초과가 발생한 것 같다.
    # X의 분자(Numerator)가 1이 되는 순간 종료함으로 해결하였다.
    while(X.numerator != 1):

        # 2배씩 증가시켜 속도를 향상시킨다.
        while(Fraction(1, tmp) > X):
            tmp *= 2

        # 1/tmp가 X미만이 되면 1회 뒤로 돌아가 선형탐색한다.
        if(Fraction(1, tmp) < X):
            tmp //= 2
            while(Fraction(1, tmp) > X):
                tmp += 1

        X -= Fraction(1, tmp)

    # 분자가 1이 된 X의 분모(Denominator)를 출력한다.
    print(X.denominator)
