"""
문제 정보
    https://www.acmicpc.net/problem/10799
    *

작성
    양승현
    2023 02 07
"""

import sys
input = sys.stdin.readline

seq = input()
opens = closes = res = 0
prev = ''

for x in seq:
    if x == '(': opens += 1
    if x == ')':
        closes += 1
        if prev == '(': res += (opens - closes)
        else: res += 1

    prev = x

print(res)




