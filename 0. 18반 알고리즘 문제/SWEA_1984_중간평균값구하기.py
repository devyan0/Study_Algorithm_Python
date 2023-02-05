"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pw_-KAdcDFAUq
    *
작성
    양승현
    2023 02 05
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    nums = sorted([int(x) for x in input().split()])
    nums[0], nums[-1] = 0, 0
    print(f'#{test_case} {round(sum(nums)/(len(nums)-2))}')
