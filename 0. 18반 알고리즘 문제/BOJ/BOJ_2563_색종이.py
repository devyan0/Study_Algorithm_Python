N = int(input())
SIDE = 100
dp = [[0 for _ in range(SIDE+1)] for _ in range(SIDE+1)]

for _ in range(N):
    i, j = map(int, input().split())
    dp[i][j] += 1
    dp[i+10][j+10] += 1
    dp[i][j+10] -= 1
    dp[i+10][j] -= 1

for j in range(1, SIDE+1):
    for i in range(1, SIDE+1):
        dp[i][j] += dp[i-1][j]

cnt = 0
for i in range(1, SIDE+1):
    for j in range(1, SIDE+1):
        dp[i][j] += dp[i][j-1]
        cnt += 1 if dp[i][j] else 0

print(cnt)
