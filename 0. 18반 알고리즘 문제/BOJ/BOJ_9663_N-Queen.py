"""
문제 정보
    https://www.acmicpc.net/problem/9663
    * fast think of -> if loc[i-k] == j-k: return False
    * think of
    * 1) each step up to above row
    * 2) bound condition: left=0, right=N-1 => subtract and add 1
    *    take this for granted

작성
    양승현
    2023 02 10
"""

N = int(input())
loc = [-1 for _ in range(N)]
cnt = 0

def valid(i, j):
    # check col
    if j in loc: return False
    for k in range(min(i, j)+1):
        if loc[i-k] == j-k: return False
    for k in range(min(i, N-1-j)+1):
        if loc[i-k] == j+k: return False
    return True

def bt(i):
    global cnt

    if i == N:
        cnt += 1
        return

    for j in range(N):
        if valid(i, j):
            loc[i] = j
            bt(i+1)
            loc[i] = -1

bt(0)
print(cnt)




