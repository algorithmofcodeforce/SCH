# Backjoon Online Judge No.3048 - 개미
# Python

l, r = map(int, input().split())
left = input()[::-1]  # 마주보는 상황이므로 거꾸로 받는다.
right = input()
t = int(input())

# Swap을 위해 list로 변환한다.
path = list(left + right)

while t:
    # While문의 탈출조건 및 인덱싱을 위한 변수 선언
    i = 0

    while(i < len(path) - 1):

        # 서로 반대 방향인 경우
        if path[i] in left and path[i + 1] in right:

            # Swap
            tmp = path[i]
            path[i] = path[i + 1]
            path[i + 1] = tmp

            # Swap 이후에는 바로 다음 문자를 조사하지 않는다
            i += 2
        # 반대방향이 아닌 경우 다음 문자를 조사한다
        else:
            i += 1
    t -= 1

print(''.join(path))
