import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappush as push, heappop as pop

N = int(input())
graph = [[int(x) for x in input().split()] for _ in range(N)]

q = [(0, 0, 1)]     # cost, cur, vis
dp = [[float('inf') for _ in range(1 << N)] for _ in range(N)]

while q:
    cost, cur, vis = pop(q)
    key = (cur, vis)



    if vis == (1 << N)-1:
        if graph[cur][0]:
            print(cost+graph[cur][0])
            exit()
        continue

    for nex in range(N):
        if not graph[cur][nex] or ((1 << nex) & vis): continue
        push(q, (cost + graph[cur][nex], nex, vis | (1 << nex)))


