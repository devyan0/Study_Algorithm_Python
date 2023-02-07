"""
문제 정보
    https://www.acmicpc.net/problem/1244
    * 출력 정보 특이함 문제 요구사항 잘 파악하고 구현 필요

작성
    양승현
    2023 02 07
"""

import sys
input = sys.stdin.readline

# take test inputs
L = int(input())
lights = [int(x) for x in input().split()]
N = int(input())

for _ in range(N):
    # gender and 1-base index
    gen, k = map(int, input().split())

    if gen == 1:
        # case 1: flip with k steps from 0 base index k-1
        for i in range(k-1, L, k):
            lights[i] ^= 1

    if gen == 2:
        # case 2: use two pointer to check symmetry
        l, r = k-1, k-1
        lights[k-1] ^= 1
        while 0 <= l and r < L and lights[l] == lights[r]:
            lights[l] ^= 1
            lights[r] ^= 1
            l -= 1
            r += 1

# print as required
for i, n in enumerate(lights):
    print(n, end=' ')
    if (i+1) % 20 == 0: print()


