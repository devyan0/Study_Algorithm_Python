import sys
sys.stdin = open('input.txt', 'r')

seq = input()
opt, l, r = 0, 0, 0

while l < len(seq):
    while r < len(seq) and seq[r] == 'R':
        r += 1

    if 0 < l and r < len(seq) and seq[l-1] == 'K' and seq[r] == 'K':
        opt = max(opt, r-l+2)
    else:
        opt = max(opt, r-l)

    l += 1

print(opt)