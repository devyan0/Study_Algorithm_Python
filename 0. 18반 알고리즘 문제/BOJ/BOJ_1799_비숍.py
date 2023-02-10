"""
문제 정보
    https://www.acmicpc.net/problem/1799
    *

작성
    양승현
    2023 02 10
"""

N = int(input())
poss = [[int(x) for x in input().split()] for _ in range(N)]
res = 0

occ_a = [False for _ in range(2*N)]
occ_s = [False for _ in range(2*N)]

def bt(step, cnt):
    global res
    i, j = divmod(step, N)

    if step == N**2:
        res = max(res, cnt)
        return

    if not (0<=i<N and 0<=j<N):
        return

    add, sub = i+j, i-j
    if poss[i][j] and not occ_a[add] and not occ_s[sub]:
        occ_a[add] = True; occ_s[sub] = True
        bt(step+1, cnt+1)
        occ_a[add] = False; occ_s[sub] = False
    bt(step+1, cnt)


bt(0, 0)
print(res)

"""
3
0 1 1
1 1 1
1 1 1

->4


"""

"""
10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1


ans:18


5
1 1 0 1 1
0 1 0 0 1
1 0 1 0 1
1 0 0 0 0
1 0 1 1 1


ans:8


5
0 0 0 0 0
0 1 0 1 0
1 0 0 0 1
0 1 0 1 0
0 0 0 0 0


ans:3


5
0 0 0 1 0
0 0 1 0 0
0 1 0 1 0
0 0 1 0 0
0 0 0 1 0


ans:3

"""