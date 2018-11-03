# Backjoon Online Judge No.3036 - 나머지
# Python

# 중복 제거를 위한 집합 선언
r = set()

for i in range(10):
    r.add(int(input()) % 42)

print(len(r))