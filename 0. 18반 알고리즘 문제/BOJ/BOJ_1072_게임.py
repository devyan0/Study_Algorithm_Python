X, Y = map(int, input().split())

changed = lambda w: 100*Y//X != 100*(Y+w)//(X+w)

l, r = 1, 1_000_000_000 + 1
while l < r:
    mid = (l+r)//2
    if changed(mid):
        r = mid
    else:
        l = mid + 1

if 1_000_000_000 < l:
    print(-1)
else:
    print(l)