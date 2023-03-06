import sys
sys.stdin = open('input.txt', 'r')

def dp(i, j):
    global w1, w2, target, memo
    if (i, j) in memo: return memo[(i, j)]

    if i == len(w1):
        return w2[j:] == target[i+j:]
    if j == len(w2):
        return w1[i:] == target[i+j:]

    res = False
    if w1[i] == target[i+j]:
        res = res or dp(i+1, j)

    if w2[j] == target[i+j]:
        res = res or dp(i, j+1)

    memo[(i, j)] = res
    return memo[(i, j)]

for tc in range(1, int(input())+1):
    w1, w2, target = input().split()
    memo = {}
    print(f'Data set {tc}: {"yes" if dp(0, 0) else "no"}')