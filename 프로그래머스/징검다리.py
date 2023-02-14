
def valid(arr, rm, u_bound, acc=0):
    for i, d in enumerate(arr):
        if d + acc < u_bound:
            if not rm: return False
            rm -= 1
            acc += d
        else:
            acc = 0

    return True

def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0] + rocks + [distance]
    diff = []
    for i in range(1, len(rocks)):
        diff.append(rocks[i] - rocks[i-1])

    cond = lambda k: valid(diff, n, k)
    l, r = min(diff), max(diff)+1

    while l < r:
        mid = (l+r)//2

        if cond(mid): l = mid + 1
        else: r = mid

    return l-1









args = [
    [25, [2, 14, 11, 21, 17], 2]
]
sols = [
    4
]

for arg, sol in zip(args, sols):
    res = solution(*arg)
    if res == sol: print('test passed')
    else: print(f'fail with res={res} sol={sol}')

