from bisect import bisect_left as bl
N = int(input())
seq = list(map(int, input().split()))

piles = []
for n in seq:
    if not piles:
        piles.append(n)
        continue

    i = bl(piles, n)
    if i < len(piles): piles[i] = n
    else: piles.append(n)

print(len(piles))
