"""
문제 정보
    로봇 시뮬레이션 (골드 5)
    https://www.acmicpc.net/problem/2174
    *
작성
    양승현
    2023 02 24
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
origin, res = list(range(1, N + 1)), []
i = -1

# iterate until result list if filled
while len(res) < N:
    # effective move bypassing the duplicate
    move = 0
    while move < K:
        # check if movable
        if origin[(i + 1) % N]: move += 1
        i = (i + 1) % N

    # next number found
    res.append(origin[i])
    origin[i] = 0

print('<' + ', '.join([str(n) for n in res]) + '>')