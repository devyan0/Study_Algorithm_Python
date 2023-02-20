# old failed legacy
from math import inf


def solution(n, paths, gates, summits):
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i][j] = w
        graph[j][i] = w

    def find_path(start, finish, graph=graph, n=n, summits=summits):
        visited = [False for _ in range(n + 1)]
        q = [(0, start)]
        total_cost = inf

        while q:
            cost, node = q.pop()
            if total_cost < cost:
                continue
            if node == finish:
                total_cost = min(total_cost, cost)
                continue
            elif node in summits:
                continue

            if visited[node]: continue
            visited[node] = True

            for idx, dist in enumerate(graph[node]):
                if not dist: continue
                q.append((max(cost, dist), idx))

        return total_cost

    res = []
    for s in gates:
        for e in summits:
            res.append([e, find_path(s, e)])

    return min(res, key=lambda x: x[1])