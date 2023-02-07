"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq
    *
작성
    양승현
    2023 02 04
"""

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    grid = []
    for _ in range(N):
        grid.append([int(x) for x in input().split()])

    cnt = 0
    for row in grid:
        step = 0
        for i, e in enumerate(row):
            if e == 1: step += 1
            if e == 0 and step == K:
                cnt += 1
                step = 0
            if i == N-1 and step == K:
                cnt += 1

    for row in list(zip(*grid)):
        step = 0
        for i, e in enumerate(row):
            if e == 1: step += 1
            if e == 0 and step == K:
                cnt += 1
                step = 0
            if i == N - 1 and step == K:
                cnt += 1

    print(cnt)

