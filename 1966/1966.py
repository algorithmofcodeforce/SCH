# Backjoon Online Judge No.1966
# Python


case = int(input())

for i in range(case):
    dnum, target = map(int, input().split())
    docs = list(map(int, input().split()))

    # Target문서의 위치를 따로 관리한다.
    location = ['']*dnum
    location[target] = 'A'
    
    cnt = 0
    
    while(len(docs) > 0):
        if docs[0] < max(docs):
            docs.append(docs.pop(0))
            location.append(location.pop(0))
        else:
            cnt += 1
            docs.pop(0)
            if(location.pop(0) == 'A'):
                break

    print(cnt)
