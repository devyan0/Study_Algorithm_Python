import sys
sys.stdin = open('s_input.txt', 'r')

def str_to_code(s):
    code = []
    for c in s:
        if c == 'a': r = int('1000', 2)
        if c == 'c': r = int('0100', 2)
        if c == 'g': r = int('0010', 2)
        if c == 't': r = int('0001', 2)
        else: r = int('1111', 2)
        code.append(r)
    return code

N, M = map(int, input().split())
seqs = [input() for _ in range(N)]

kinds = [1] * M

for i in range(M):
    show = set(s[i] for s in seqs) - {'.'}
    kinds[i] = max(1, len(show))

print(max(kinds))
