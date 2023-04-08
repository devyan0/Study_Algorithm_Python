import sys
sys.stdin = open('input.txt', 'r')

"""
N: number of computers (nodes)
M: number of connections (edges)
"""
import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(set)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].add(a)

dp = [0] * (N+1)

def dfs(n, visit):
    if not graph[n] - visit:
        dp[n] = 1
        return dp[n]

    dp[n] = max(dp[n], 1 + max([dfs(child, visit | {n}) for child in graph[n]] + [1]))
    return dp[n]

for n in range(1, N+1):
    dfs(n, set())

print(dp)
max_depth = max(dp)
print([i for i in range(1, N+1) if dp[i] == max_depth])
