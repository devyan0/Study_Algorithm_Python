import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappush as push, heappop as pop

def bfs(graph, start, dest):
    q = [(0, start)]  # cost, node
    min_dist = float('inf')
    vis = set()

    while q:
        dist, cur = pop(q)
        if cur == dest:
            if min_dist < dist:
                return dist
            else:
                min_dist = dist
                continue

        if cur in vis: continue
        vis.add(cur)

        for next_, cost in enumerate(graph[cur]):
            if cost == float('inf'): continue
            push(q, (dist + cost, next_))

    return -1

while True:
    V, E = map(int, input().split())
    if (V, E) == (0, 0): exit()

    start, dest = map(int, input().split())
    graph = [[float('inf') for _ in range(V)] for _ in range(V)]
    for _ in range(E):
        u, v, p = map(int, input().split())
        graph[u][v] = p

    res = bfs(graph, start, dest)
    print(res)






