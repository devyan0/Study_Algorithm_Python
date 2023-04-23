import sys
sys.stdin = open('input.txt', 'r')

from itertools import accumulate

N, M = map(int, input().split())
nums = map(int, input().split())
acc = [0] + list(accumulate(nums))

l, r = 0, 1
cnt = 0

while r < len(acc):
    partial_sum = acc[r] - acc[l]
    if partial_sum == M:
        cnt += 1

    if partial_sum < M:
        r += 1
    else:
        l += 1

print(cnt)

