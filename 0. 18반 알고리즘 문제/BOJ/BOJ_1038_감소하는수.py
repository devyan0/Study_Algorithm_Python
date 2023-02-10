"""
문제 정보
    https://www.acmicpc.net/problem/1038
    *

작성
    양승현
    2023 02 10
"""

N = int(input())
cnt = 0
res = -1

def bt(dep, temp):
    global cnt, res
    if 0 < res: return

    if dep == 7:
        cnt += 1
        print(cnt, temp)
        if cnt == N:
            res = int(''.join([str(x) for x in temp]))

        return

    bt(dep + 1, temp)
    for i in range(10):
        if not temp or temp[-1] > i:
            bt(i+1, temp + [i])




bt(0, [])
print(res)