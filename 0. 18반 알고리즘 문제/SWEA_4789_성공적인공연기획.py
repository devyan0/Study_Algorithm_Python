"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWS2dSgKA8MDFAVT
    *
작성
    양승현
    2023 02 05
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    claps, sum_, need = [int(x) for x in input()], 0, 0
    for i, n in enumerate(claps):
        if sum_ < i:
            need += (i-sum_)
            sum_ = i
        sum_ += n

    print(f'#{test_case} {need}')
