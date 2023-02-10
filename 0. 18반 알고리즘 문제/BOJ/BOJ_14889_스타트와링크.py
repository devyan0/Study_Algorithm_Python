"""
문제 정보
    https://www.acmicpc.net/problem/14889
    * 2N = N + N condition

작성
    양승현
    2023 02 10
"""

N = int(input())
abil = [[int(x) for x in input().split()] for _ in range(N)]
pick = [False for _ in range(N)]
res = float('inf')

def bt(i, temp):
    global res

    # branch if timeout

    if i == N:
        if sum(pick) == N//2:
            res = min(res, abs(temp))
        return

    # say, selecting 3rd -> check 1st, 2nd ability
    add = 0
    sub = 0
    for j in range(i):
        if pick[j]:
            add += abil[i][j] + abil[j][i]
        else:
            sub += abil[i][j] + abil[j][i]

    pick[i] = True
    bt(i+1, temp+add)
    pick[i] = False
    bt(i+1, temp-sub)



bt(0, 0)
print(res)

