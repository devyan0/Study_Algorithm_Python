"""
문제 정보
    https://www.acmicpc.net/problem/2776
    * solution using pointer (yet)

작성
    양승현
    2023 02 09
"""

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    l1 = int(input()); note1 = [int(x) for x in input().split()]
    l2 = int(input()); note2 = [int(x) for x in input().split()]
    recon = {x: i for i, x in enumerate(note2)}

    p1 = p2 = 0
    exists = [False for _ in range(l2)]

    note1.sort(); note2.sort()

    while p2 < l2:
        exists[recon[note2[p2]]] = note1[p1] == note2[p2]
        p2 += 1
        while p1+1 < l1 and note1[p1+1] <= note2[p2]: p1 += 1


    for e in exists:
        print(1 if e else 0)

