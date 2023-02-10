"""
문제 정보
    https://www.acmicpc.net/problem/12865
    * not at once, couldn't find where is wrong
    * should recap

작성
    양승현
    2023 02 10
"""

N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, input().split())
    for k in range(K+1):
        if 0 <= k-W:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-W]+V)
        else:
            dp[i][k] = dp[i - 1][k]

print(dp[-1][-1])

"""
5 10
9 5
4 8
8 9
7 8
5 3


-> 16 wrong
-> 11
"""