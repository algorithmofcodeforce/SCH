# Backjoon Online Judge No.2309 - 일곱 난쟁이
# Python

def search():
    total = sum(hobits)
    for i in range(9):
        for j in range(i+1, 9):
            if(hobits[i] + hobits[j] == total - 100):
                return (hobits[i], hobits[j])

hobits = []

for i in range(9):
    hobits.append(int(input()))

f1, f2 = search()
hobits.remove(f1)
hobits.remove(f2)

hobits.sort()
for i in range(7):
    print(hobits[i])
