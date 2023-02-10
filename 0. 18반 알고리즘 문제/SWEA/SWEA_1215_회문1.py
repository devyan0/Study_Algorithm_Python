"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi
    * two pointer

작성
    양승현
    2023 02 06
"""
import sys
sys.stdin = open("input.txt", "r")
"""
5
CBCABBAC
BBABCCBA
ABCBCCCA
BACCAABB
BCBCACBC
CABACACB
CAAACCAB
CBABACAC

1
AAAAAAAA
AAAAAAAA
AAAAAAAA
AAAAAAAA
AAAAAAAA
AAAAAAAA
AAAAAAAA
AAAAAAAA

"""

def line_check(line, L):
    l, r = 0, L-1
    count = 0

    while r < len(line):
        ll, rr = l, r
        while line[ll] == line[rr]:
            if ll >= rr:
                count += 1
                break
            ll += 1
            rr -= 1

        l, r = l+1, r+1

    return count

for test_case in range(1, 11):
    L = int(input())
    cnt, grid = 0, []

    for _ in range(8):
        grid.append([x for x in input()])

    cnt = 0
    for row in grid:
        cnt += line_check(row, L)
    for col in zip(*grid):
        cnt += line_check(col, L)

    print(f'#{test_case} {cnt}')


