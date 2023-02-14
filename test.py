"""
문제 정보
    https://www.acmicpc.net/problem/15732
    * filter condition

작성
    양승현
    2023 02 09
"""

N, K, D = map(int, input().split())
info, l, r = [list(map(int, input().split())) for _ in range(K)], 1, N+1
prev_cnt = lambda n: sum(filter(lambda k: 0 < k, [1 + (min(n, x[1])-x[0])//x[2] for x in info]))
while l < r:
    mid = (l+r) // 2
    cnt = prev_cnt(mid)
    if cnt >= D: r = mid
    else: l = mid + 1
print(l)