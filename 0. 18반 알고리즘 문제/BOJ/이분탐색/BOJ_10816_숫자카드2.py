"""
https://www.acmicpc.net/problem/10816
라이브러리 사용법
"""
from bisect import bisect_left as bl, bisect_right as br
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

cnt = lambda n: br(cards, n) - bl(cards, n)

M = int(input())
counts = [cnt(n) for n in map(int, input().split())]
[print(x, end=' ') for x in counts]