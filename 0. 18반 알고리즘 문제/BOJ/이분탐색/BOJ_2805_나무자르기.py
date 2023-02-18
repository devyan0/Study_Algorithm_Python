import sys
input = sys.stdin.readline

_, NEED = map(int, input().split())
arr = [int(x) for x in input().split()]

valid = lambda cut: NEED <= sum([max(0, x-cut) for x in arr])

l, r = 0, max(arr)+1
while l < r:
    mid = (l+r) // 2
    if valid(mid):
        l = mid+1
    else:
        r = mid

print(l-1)


"""
import sys
i = sys.stdin.readline
_, N = map(int, i().split())
a = [int(x) for x in i().split()]
v = lambda c: N <= sum([max(0, x-c) for x in a])
l, r = 0, max(a)
while l<r:
    m = (l+r) // 2
    if v(m):l=m+1
    else:r=m
print(l-1)
"""

