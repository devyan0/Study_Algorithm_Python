"""
문제 정보
    https://www.acmicpc.net/problem/1987
    *

작성
    양승현
    2023 02 09
"""
import time

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [[x for x in input()] for _ in range(R)]
res = 0
def bt(r, c, visited):
    global res

    res = max(res, len(visited))

    cur = board[r][c]
    if cur in visited:
        return

    res = max(res, len(visited))

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if not (0<=nr<R and 0<=nc<C): continue

        # overhead here: O(len(visited) + len(cur))
        # <= O(26 + 1) = O(1) but .. optimization required...
        # hate this
        bt(nr, nc, visited | {cur})


START = time.time()

bt(0, 0, set())

print(res)

print(f'{(time.time()-START)*1000*1000*1000:.0f} ns')
#
#
"""
20 20
qwertyuioplkjhgfdsaz
12345678901234567890
mnbvcxzlkjhgfdsaqwer
l12345d5d4f4d8s7e5f4
d4f8d4s5df4sd6af54ds
dfa68sdf8as46derewr7
das6d8f7as6d8f7avxcg
gfhd687jdfgl6gi8lli8
g8ag768dsv77gaaer8t8
8f7g768b7df68g7s688r
sd6g8787ta6w8e7rd8fa
8g7f6d8asd7tyrwt8re7
qweq87r8we7tq87vcbgh
jhj8gfk7uy87iytj8hgg
dfg87sdh87yj7k8u8gh7
h7g8dfgj76dy8j7d8g7h
s687sdcxbdtuwryteu77
sdfg87er78ytwy7d4h3h
h4sdfs3df4h8fhsdfh4f
sdh423fsdh45fhs4f5h4
df5h4sdf68h7hhjdfjdf
y8we7687ery864g6fs4f
6fdh54s6fh54s6d54h55
zcxbz3xcb1xcb1z3x2cb
tq87987yw9re8y7we98r
54fa6sd4f56as4df6fff
36

Process finished with exit code 0

20 20
abcdefghijklmnopqrsaz
fghijklmnopqrstuvwxaz
klmnopqrstuvwxyabcdaz
pqrstuvwxyabcdefghiaz
bcdefghijklmnopqrstaz
cdefghijklmnopqrstuaz
vkaljsdfoweuqowijklaz
vlxciuevoiqnewrlaacaz
abcdefghijklmnopqrsaz
fghijklmnopqrstuvwxaz
klmnopqrstuvwxyabcdaz
pqrstuvwxyabcdefghiaz
uvwxyabcdefghijklmnaz
bcdefghijklmnopqrstaz
cdefghijklmnopqrstuaz
qwoeirumadxcnaskfhoaz
vkaljsdfoweuqowijklaz
vlxciuqvoiqnewrlavcaz
qoeiwueoinmcfaslkfaaz
zcxbz3xcb1xcb1z3x2cb
tq87987yw9re8y7we98r
54fa6sd4f56as4df6fff

10 10
IEFCJPOIDH
FHFKCPOIDH
FFALFPOIDH
HFGCFPOIDH
HMCHHPOIDH
IEFCJPOIDH
FHFKCPOIDH
FFALFPOIDH
HFGCFPOIDH
HMCHHPOIDH

"""