from collections import defaultdict

def solution(edges, target):
    graph = defaultdict(list)
    dirs = defaultdict(int)

    for p, c in edges:
        graph[p].append(c)

    def pprint():
        for k in graph:
            print(k, graph[k])
        print()

    # pprint()
    # for p in graph.copy():
    #     while len(graph[p]) == 1:
    #         c = graph[p][0]
    #         if graph[c]:
    #             graph[p] = graph[c]
    #         else: break

    # pprint()



    def inc_dir(n=1):
        while graph[n]:
            child = graph[n][dirs[n]]
            dirs[n] = (dirs[n] + 1) % len(graph[n])
            n = child
        return n

    def dec_dir(n=1):
        while graph[n]:
            dirs[n] = (dirs[n] - 1) % len(graph[n])
            child = graph[n][dirs[n]]
            n = child

    res = None
    acc = [0] * (len(edges)+2)
    target = [0] + target

    def bt(put):
        nonlocal res
        if acc == target:
            if not res or len(put) < len(res):
                print(f'\tfound new result of {put}')
                res = put
            return

        # if put == [3, 2, 1, 1]:
        #     print('check')

        for i in [1, 2, 3]:
            leaf = inc_dir()
            if acc[leaf] + i <= target[leaf]:
                acc[leaf] += i
                print(f'now put {i} to {leaf} -> put: {str(put + [i]):<25} acc: {acc}')
                bt(put+[i])
                acc[leaf] -= i
            dec_dir()

    bt([])
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
        print(f'result {res} differ from {s}')
    else:
        print(f'test passed')
print('test finished')