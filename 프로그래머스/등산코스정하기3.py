from collections import defaultdict, deque

def solution(n, paths, gates, summits):
    summits.sort()
    d = defaultdict(lambda: defaultdict(int))
    for p in paths:
        n1, n2, w = p
        d[n1][n2] = w
        d[n2][n1] = w

    excld = set(summits)
    gout = set(gates)

    def search(s, lim):
        q = deque([s])
        vis = set()
        while q:
            node = q.popleft()
            if node in gout:
                return True

            # do not meet other gates or summits
            elif node != s and node in excld: continue

            if node in vis: continue
            vis.add(node)

            for child in d[node]:
                cost = d[node][child]
                if lim < cost: continue
                q.append(child)

        return False

    def valid(lim):
        for s in summits:
            if search(s, lim):
                return s

        return -1

    MAX_R = max(paths, key=lambda x: x[-1])[-1]
    l, r = 0, MAX_R+1
    while l < r:
        mid = (l+r)//2
        sm = valid(mid)
        if 0 <= sm:
            r = mid
        else:
            l = mid + 1

    # l = min(l, MAX_R)
    return [valid(l), l]


args = [
    [6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]],
    [7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]],
    [7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]],
    [5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]],
]

sols = [
    [5, 3],
    [3, 4],
    [5, 1],
    [5, 6]
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')