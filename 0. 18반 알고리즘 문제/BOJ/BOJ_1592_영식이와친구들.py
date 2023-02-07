"""
문제 정보
    https://www.acmicpc.net/problem/1592
    *

작성
    양승현
    2023 02 07
"""

import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
receive, cur, cnt = [0 for _ in range(N)], 0, 0

while receive[cur] < M:
    if receive[cur] % 2:
        cur = (cur + L) % N
    else:
        cur = (cur - L) % N

    receive[cur] += 1
    cnt += 1

print(cnt-1)

