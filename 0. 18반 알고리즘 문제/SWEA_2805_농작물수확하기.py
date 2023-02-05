"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB
    *
작성
    양승현
    2023 02 05
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, grid = int(input()), []

    for _ in range(N):
        grid.append([int(x) for x in input()])

    center, sum_ = N // 2, 0
    for i in range(N):
        for j in range(N):
            if abs(i-center) + abs(j-center) <= center:
                sum_ += grid[i][j]

    print(f'#{test_case} {sum_}')

