import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        print(0 if len(q) else 1)
    elif cmd[0] == 'front':
        print(q[0] if q else -1)
    elif cmd[0] == 'back':
        print(q[-1] if q else -1)
