import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
from heapq import heappush as push, heappop as pop

def search(d, N, M):
    q = deque()
    q.append((0, 0, 1))    # cost, time, node
    min_time = float('inf')
    memo = [(float('inf'), float('inf')) for _ in range(1, N+1)]
    while q:
        cost, time, node = q.popleft()
        if node == N:
            min_time = min(min_time, time)
            continue

        if memo[node][0] < cost and memo[node][1] < time: continue


        for next_node in range(1, N+1):
            if d[node][next_node][0] == float('inf'):
                continue
            next_cost = cost + d[node][next_node][0]
            next_time = time + d[node][next_node][1]
            if next_cost <= M:
                q.append((next_cost, next_time, next_node))

    return min_time

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())     # N: number of nodes, M: budget, K: number of edges
    edges = [list(map(int, input().split())) for _ in range(K)]     # u, v, cost, time

    d = [[(float('inf'), float('inf')) for _ in range(N+1)] for _ in range(N+1)]
    for n1, n2, cost, time in edges:
        d[n1][n2] = (cost, time)
        d[n2][n1] = (cost, time)

    min_dist = search(d, N, M)
    print(min_dist if min_dist < float('inf') else 'Poor KCM')

