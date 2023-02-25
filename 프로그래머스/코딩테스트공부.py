
def solution(alp, cop, problems):
    A = max(problems, key=lambda x: x[0])[0]
    C = max(problems, key=lambda x: x[1])[1]
    dp = [[float('inf') for _ in range(C+1)] for _ in range(A+1)]
    # alp = min(alp, A)
    # cop = min(cop, C)

    dp[alp][cop] = 0
    for a in range(alp, A+1):
        for c in range(cop, C+1):
            if a+1 <= A: dp[a+1][c] = min(dp[a+1][c], dp[a][c]+1)
            if c+1 <= C: dp[a][c+1] = min(dp[a][c+1], dp[a][c]+1)

            for areq, creq, arwd, crwd, cost in problems:
                if areq <= a and creq <= c:
                    na, nc = min(a+arwd, A), min(c+crwd, C)
                    dp[na][nc] = min(dp[na][nc], dp[a][c]+cost)

    for d in dp:
        print(d)

    return dp[A][C]





args = [
    [	10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]],
    [0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]]
]

sols = [
    15,
    13
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')