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

def check(i, j, board):
    d = {}
    for k in range(9):
        val = board[i][k]
        if d.setdefault(val, 0): return False
        d[val] += 1

    d = {}
    for k in range(9):
        val = board[k][j]
        if d.setdefault(val, 0): return False
        d[val] += 1

    bi, bj = i//3, j//3
    d = {}
    for i_ in range(3):
        for j_ in range(3):
            val = board[3*bi+i_][3*bj+j_]
            if d.setdefault(val, 0): return False
            d[val] += 1

    return True


T = int(input())

for test_case in range(1, T + 1):
    board = []
    for _ in range(9):
        board.append([int(x) for x in input().split()])

    res = True
    for i in range(9):
        for j in range(9):
            if not res: continue
            if not check(i, j, board):
                res = False

    print(f'#{test_case} {1 if res else 0}')
