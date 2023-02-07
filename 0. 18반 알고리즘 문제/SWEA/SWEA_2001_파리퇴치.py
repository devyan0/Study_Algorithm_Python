"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq
    *
작성
    양승현
    2023 02 05
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    grid = []
    for _ in range(N):
        grid.append([int(x) for x in input().split()])

    res = 0
    for i in range(M-1, N):
        for j in range(M-1, N):
            kill = 0
            for x in range(M):
                for y in range(M):
                    kill += grid[i-x][j-y]
            res = max(res, kill)

    print(f'#{test_case} {res}')
