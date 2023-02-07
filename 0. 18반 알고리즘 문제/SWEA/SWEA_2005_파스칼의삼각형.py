"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq
    *
작성
    양승현
    2023 02 05
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            dp[i][j] += dp[i-1][j]
            if j > 0: dp[i][j] += dp[i-1][j-1]

    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            if dp[i][j]: print(dp[i][j], end=' ')
        print()

