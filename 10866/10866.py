# Backjoon Online Judge No.10866
# Python
import sys

deque = []


def push_front(x):
    deque.insert(0, x)


def push_back(x):
    deque.append(x)


def pop_front():
    if deque:
        print(deque.pop(0))
    else:
        print(-1)


def pop_back():
    if deque:
        print(deque.pop())
    else:
        print(-1)


def size():
    print(len(deque))


def empty():
    if not deque:
        print(1)
    else:
        print(0)


def front():
    if deque:
        print(deque[0])
    else:
        print(-1)


def back():
    if deque:
        print(deque[-1])
    else:
        print(-1)


N = int(input())
commands = []


for i in range(N):
    commands.append(sys.stdin.readline().rstrip())
for s in commands:
    cmd = s.split()
    if len(cmd) == 1:
        locals()[cmd[0]]()
    else:
        locals()[cmd[0]](int(cmd[1]))