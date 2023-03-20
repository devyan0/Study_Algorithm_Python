import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop as pop, heappush as push

T = int(input())
for tc in range(1, T+1):
    K, s = int(input()), input()
    temp, q = '', []

    for i in range(len(s)-1, -1, -1):
        temp += s[i]
        push(q, temp)

    res = ''
    for _ in range(K):
        res = pop(q)

    print(f'#{tc} {res}')

