import sys
input = sys.stdin.readline

_, NEED = map(int, input().split())
arr = [int(x) for x in input().split()]

def unboxing(condition):
    """
    condition은 자르는 높이
    arr에 있는 높이로 잘랐을 때 가져갈 수 있는 나무 수 계산
    필요한 나무 수 NEED보다 크면 True 반환
    """
    take = 0
    for h in arr:
        if h < condition:   # 작으면 못가져감
            take += 0
        else:               # 잘린 부분만 가져감
            take += (h-condition)

    return NEED <= take      # 가능하면 True

l, r = 0, max(arr)+1
while l < r:
    mid = (l + r) // 2
    if unboxing(mid) == True:
        l = mid + 1
    else:
        r = mid

print(l-1)
