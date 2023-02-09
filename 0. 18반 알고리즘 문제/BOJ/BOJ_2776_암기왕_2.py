"""
문제 정보
    https://www.acmicpc.net/problem/2776
    * binary search

작성
    양승현
    2023 02 09
"""
from bisect import bisect_left as bs
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    l1 = int(input()); note1 = [int(x) for x in input().split()]
    l2 = int(input()); note2 = [int(x) for x in input().split()]
    note1.sort()

    def in_note1(x):
        i = bs(note1, x)
        return note1[i if i < l1 else -1] == x

    for x in note2:
        print(1 if in_note1(x) else 0)


