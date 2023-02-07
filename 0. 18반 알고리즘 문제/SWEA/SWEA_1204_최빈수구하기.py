"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh
    *

작성
    양승현
    2023 02 06
"""
import sys
sys.stdin = open("input.txt", "r")

from collections import Counter

T = int(input())

for test_case in range(1, T+1):
    _ = int(input())
    scores = Counter(input().split())
    print(f'#{test_case} {scores.most_common()[0][0]}')

