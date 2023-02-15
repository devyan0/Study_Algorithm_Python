from bisect import bisect_left as bs
import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

piles = []
for n in seq:
    if not piles:
        piles.append(n)
        continue

    i = bs(piles, n)
    if i == len(piles): piles.append(n)
    else: piles[i] = n

print(len(piles))