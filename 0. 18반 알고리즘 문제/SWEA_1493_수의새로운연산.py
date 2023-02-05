"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq
    *
작성
    양승현
    2023 02 04
"""

import sys
sys.stdin = open("input.txt", "r")

def rotate(grid):
    N = len(grid)
    res = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[j][N-1-i] = grid[i][j]

    return res


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append([int(x) for x in input().split()])

    grid90 = rotate(grid)
    grid180 = rotate(grid90)
    grid270 = rotate(grid180)

    print(f'#{test_case}')
    for i in range(N):
        for g in [grid90, grid180, grid270]:
            for j in range(N):
                print(f'{g[i][j]}', end='')
            print('', end=' ')
        print()

