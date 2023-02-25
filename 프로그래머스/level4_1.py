
def solution(cookie):
    N = len(cookie)
    lc, rc = [None] * N, [None] * N
    dp = [[0 for _ in cookie] for _ in cookie]
    for i in range(N-1, -1,- 1):
        for j in range(i, N):
            if i == j:
                dp[i][j] = cookie[i]
            else:
                dp[i][j] = dp[i][j-1] + cookie[j]

    for i in dp:
        print(i)
    print()

    temp = set()
    for r in range(N):
        lc[r] = temp
        for l in range(r+1):
            temp = temp | {dp[l][r]}

    print(lc)

    temp = set()
    for l in range(N-1, -1, -1):
        for r in range(N):
            temp = temp | {dp[l][r]}
        rc[l] = temp
    print(rc)


    res = 0
    for mid in range(N):
        inter = lc[mid] & rc[mid]
        if inter: res = max(res, max(inter))
        # print(mid, lc[mid] & rc[mid])

    return res





args = [
    [	[1, 1, 2, 3]],
    [	[1, 2, 4, 5]]
]

sols = [
    3,
    0
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')