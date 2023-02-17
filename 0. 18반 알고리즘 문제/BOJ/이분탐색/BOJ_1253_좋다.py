from bisect import bisect_left as bl, bisect_right as br
from itertools import accumulate
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(x) for x in input().split()]
nums.sort()

visited = set()
good = [0] * (N+1)
for i in range(N):
    for j in range(i+1, N):
        find = nums[i] + nums[j]
        if nums[i] == nums[j]: continue
        if find in visited: continue

        r = br(nums, find)
        l = bl(nums, find)
        l = max(l, j+1)
        if l != r:
            visited.add(find)
            good[l] += 1
            good[r] -= 1

print(sum(accumulate(good)))

