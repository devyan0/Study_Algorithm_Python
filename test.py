"""
https://www.acmicpc.net/problem/2470
https://www.acmicpc.net/problem/2467
TP 문제
    오답 1: l <= r -> l < r : 서로 다른이라는 조건
    오답 2: r = len(sols)-1 two pointer로 접근
    오답 3: res = [mix, -> res = [abs(mix) 실수
"""
import bisect
import sys
input = sys.stdin.readline

N = int(input())
sols = list(map(int, input().split()))

l, r = 0, len(sols)-1
res = [float('inf'), [l, r]]

while l < r:
    mix = sols[l] + sols[r]

    if abs(mix) <= res[0]:
        res = [abs(mix), [l, r]]

    if 0 < mix: r -= 1
    else: l += 1

print(*[sols[p] for p in res[1]])