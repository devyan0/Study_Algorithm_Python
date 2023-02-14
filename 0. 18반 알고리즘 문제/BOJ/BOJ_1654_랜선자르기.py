import sys
input = sys.stdin.readline

K, NEED = map(int, input().split())
wires = [int(input()) for x in range(K)]

valid = lambda cut: NEED <= sum([x//cut for x in wires])
l, r = 1, max(wires)+1

while l < r:
    mid = (l+r)//2
    if valid(mid):
        l = mid+1
    else:
        r = mid

print(l-1)
