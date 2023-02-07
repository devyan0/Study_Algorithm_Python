"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ
    *

작성
    양승현
    2023 02 06
"""
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append([1 if x=='o' else 0 for x in input()])

    res = False
    res = res or any([all(row) for row in grid])
    res = res or any([all(row) for row in zip(*grid)])
    res = res or all([grid[i][i] for i in range(5)])
    res = res or all([grid[i][4-i] for i in range(5)])

    print(f'#{test_case} {"YES" if res else "NO"}')
