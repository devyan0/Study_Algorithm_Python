import sys
input = sys.stdin.readline

N = int(input())
reqs = list(map(int, input().split()))
target = int(input())

get_req = lambda bound: sum([min(bound, x) for x in reqs])

l, r = 1, max(reqs)+1
while l < r:
    mid = (l+r)//2
    if target < get_req(mid):
        r = mid
    else:
        l = mid+1

print(l-1)