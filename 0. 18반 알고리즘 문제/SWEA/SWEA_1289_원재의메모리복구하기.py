"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN
    *
작성
    양승현
    2023 02 04
"""

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    target = input()
    prev, cnt = '0', 0
    for c in target:
        if c != prev: cnt += 1
        prev = c

    print(f'#{test_case} {cnt}')
