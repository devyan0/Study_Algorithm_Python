"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD
    *

작성
    양승현
    2023 02 06
"""
import sys
sys.stdin = open("input.txt", "r")


for test_case in range(1, 11):
    N = int(input())
    seq = input()
    opens = [0, 0, 0, 0] # ( [ { <
    valid = True

    for i, chk in enumerate(seq):
        if chk == '(': opens[0] += 1
        if chk == '[': opens[1] += 1
        if chk == '{': opens[2] += 1
        if chk == '<': opens[3] += 1

        if chk == ')':
            opens[0] -= 1
            if opens[0] < 0: valid = False
        if chk == ']':
            opens[1] -= 1
            if opens[1] < 0: valid = False
        if chk == '}':
            opens[2] -= 1
            if opens[2] < 0: valid = False
        if chk == '>':
            opens[3] -= 1
            if opens[3] < 0: valid = False

    print(f'#{test_case} {1 if valid else 0}')












