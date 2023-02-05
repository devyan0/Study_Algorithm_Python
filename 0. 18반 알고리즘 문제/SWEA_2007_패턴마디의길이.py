"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq
    *
작성
    양승현
    2023 02 05
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    seq, res = input(), 0

    for i in range(1, 11):
        if res: continue
        good = True
        for j in range(i):
            good = good and (seq[j] == seq[i+j])
        if good: res = i

    print(f'#{test_case} {res}')

