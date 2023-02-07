"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm
    *

작성
    양승현
    2023 02 06
"""
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())


for test_case in range(1, T + 1):
    seq = input()
    o = c = res = 0

    prev = ''
    for x in seq:
        if x == '(': o += 1
        if x == ')':
            c += 1
            if prev == '(': res += (o - c)
            else: res += 1

        prev = x

    print(f'#{test_case} {res}')













