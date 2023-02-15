from bisect import bisect_left as bs
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# N = 10
# nums = [-61, -28, -72, 59, 13, -21, 84, -76, -52, -1]

# N = 6
# nums = [10, 20, 10, 30, 20, 50]

# N = 5
# nums = [34, -43, 32, 32, -3]

track = [-1 for _ in range(N)]
q = []

for i, n in enumerate(nums):
    if not q:
        q.append([n, i])
        continue

    k = bs(q, [n, -float('inf')])
    if k == len(q):
        q.append([n, i])
        prev_n, prev_idx = q[k - 1]
        track[i] = prev_idx

    else:
        q[k] = [n, i]
        if 0 < k:
            prev_n, prev_idx = q[k - 1]
            track[i] = prev_idx

#     print(f'=== {i} ===')
#     print(*[f'{n:4d}' for n in nums])
#     print(*[f'{n:4d}' for n in track])
#     print()
#
# print(*[f'{n:4d}' for n in nums])
# print(*[f'{n:4d}' for n in track])
# print(q)

cur = q[-1][1]  # index of last pile
backward = []
while 0 <= cur: # not 0 < cur ...
    backward.append(nums[cur])
    cur = track[cur]

print(len(backward))
print(*backward[::-1])

"""
Input:
10
-61 -28 -72 59 13 -21 84 -76 -52 -1

Output:
4
-76 -28 -21 -1

Answer:
4
-61 -28 -21 -1



5
34 -43 32 32 -3

3
wrong: -3 -43 -3
"""


