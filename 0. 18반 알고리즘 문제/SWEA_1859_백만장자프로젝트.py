"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc
    *
작성
    양승현
    2023 02 04
"""

T = int(input())

for test_case in range(1, T + 1):
    res, N, pr = 0, int(input()), [int(x) for x in input().split()]

    # two pointer
    l, r, profit = N - 1, N - 1, 0

    while 0 <= l:
        while 0 <= l and pr[l] <= pr[r]:
            profit += pr[r] - pr[l]
            l -= 1

        r = l

    print(f'#{test_case} {profit}')
