import sys
sys.stdin = open('input.txt', 'r')

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100_000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(set)
indegree = defaultdict(int)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    indegree[b] += 1

q = deque([i for i in range(1, N + 1) if indegree[i] == 0])

depth = {i: 0 for i in range(1, N + 1)}

while q:
    node = q.popleft()
    for child in graph[node]:
        depth[child] = max(depth[child], depth[node] + 1)
        indegree[child] -= 1
        if indegree[child] == 0:
            q.append(child)

max_value = max(depth.values())
print(*sorted([i for i in depth if depth[i] == max_value]))
