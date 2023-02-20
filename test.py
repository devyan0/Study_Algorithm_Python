

dist = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],     # to 0
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],     # to # 1
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],     # to 2
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],     # to 3
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],     # to 4
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],     # to 5
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],     # to 6
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],     # to 7
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],     # to 8
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],     # to 9
]

import sys
sys.setrecursionlimit(int(1e9))

def solution(numbers):
    memo = {}

    def dp(i, l, r, temp):
        if i == len(numbers):
            return temp

        n = int(numbers[i])

        if (n, l, r) in memo and memo[(n, l, r)] < temp:
            return memo[(n, l, r)]

        d_l = dist[n][l]
        d_r = dist[n][r]

        if l == n:
            res = dp(i+1, n, r, temp + d_l)
        elif r == n:
            res = dp(i+1, l, n, temp + d_r)
        else:
            res = min(
                dp(i + 1, n, r, temp + d_l),
                dp(i + 1, l, n, temp + d_r)
            )

        memo[(n, l, r)] = res
        return res

    return dp(0, 4, 6, 0)


# args = ["1756", "5123", "151506"]
# sols = [10, 8, 15]
# for a, s in zip(args, sols):
#     res = solution(a)
#     if res != s:
#         print(f'result {res} differ from {s}')
#
# print('test finished')
