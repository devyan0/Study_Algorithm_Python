"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn
    *

작성
    양승현
    2023 02 06
"""
import sys
sys.stdin = open("s_input.txt", "r")

from itertools import accumulate

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    stops = [0] * 5002

    for i in range(1, N+1):
        a, b = map(int, input().split())
        stops[a] += 1
        stops[b+1] -= 1

    prev = 0
    stops = [n for n in accumulate(stops)]


    print(f'#{test_case}', end=' ')

    P = int(input())
    for _ in range(P):
        print(stops[int(input())], end=' ')
    print()











