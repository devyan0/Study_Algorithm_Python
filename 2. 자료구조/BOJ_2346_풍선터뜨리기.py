"""
문제 정보
    https://www.acmicpc.net/problem/22866
    * move itself can be negative

작성
    양승현
    2023 02 08
"""

"""
5
3 2 1 -3 -1
1 4 5 3 2

5
-5 -5 -5 -5 -5
1 5 3 2 4

5
5 5 5 5 5
1 2 4 5 3
"""

from collections import deque

N = int(input())
seq = [int(x) for x in input().split()]
q = deque([(x, i+1) for i, x in enumerate(seq)])

# order q to have next pop in index 0
while q:
    move, num = q.popleft()
    print(num, end=' ')
    if not q: break

    if 0 < move:
        q.rotate(-move+1)
    else:
        q.rotate(-move)
