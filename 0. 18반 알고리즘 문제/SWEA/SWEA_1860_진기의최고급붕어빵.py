"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc
    *

작성
    양승현
    2023 02 06
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())


for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arrivals = sorted([int(x) for x in input().split()])
    out = 0
    poss = True

    for t in arrivals:
        made = K * (t // M)
        if 0 < made - out:
            out += 1
        else:
            poss = False

    print(f"#{test_case} {'Possible' if poss else 'Impossible'}")
