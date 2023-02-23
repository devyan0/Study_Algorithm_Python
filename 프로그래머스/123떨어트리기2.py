from collections import defaultdict

def solution(edges, target):
    graph = defaultdict(list)
    dirs = defaultdict(int)

    for p, c in edges:
        graph[p].append(c)

    for k in graph:
        graph[k].sort()

    def inc_dir(n=1):
        while graph[n]:
            child = graph[n][dirs[n]]
            dirs[n] = (dirs[n] + 1) % len(graph[n])
            n = child
        return n


    path_cnt = 1
    for k in graph:
        path_cnt *= len(graph[k])

    seq = []
    def get_seq(i):
        i %= path_cnt
        if len(seq) <= i:
            for _ in range(i-len(seq)+1):
                seq.append(inc_dir())
        return seq[i]

    target = [0] + target
    acc = [0 for _ in target]

    res = []
    def bt(i, put):
        nonlocal res
        if res and len(res) < len(put): return
        if target == acc:
            if not res or len(put) <= len(res):
                res = put
            return

        for drop in [3, 2, 1]:
            # idx = seq[i]
            idx = get_seq(i)
            if acc[idx] + drop <= target[idx]:
                acc[idx] += drop
                bt(i+1, put+[drop])
                acc[idx] -= drop

    bt(0, [])
    return res if res else [-1]



args = [
    [[[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]], [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]],
    [[[1, 2], [1, 3]], [0, 7, 3]],
    [[[1, 3], [1, 2]], [0, 7, 1]],
]

sols = [
    [1, 1, 2, 2, 2, 3, 3],
    [1, 1, 3, 2, 3],
    [-1],
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'failed: result {res} differ from {s}')
    else:
        print(f'test passed')
print('test finished')