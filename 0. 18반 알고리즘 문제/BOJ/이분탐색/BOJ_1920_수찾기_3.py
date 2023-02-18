import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

def search(target):
	# 열린 범위
    l, r = 0, len(nums)
    while l < r:
        mid = (l+r)//2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l = mid + 1
        elif target < nums[mid]:
            r = mid

    return False

K = int(input())
finds = map(int, input().split())
for to_find in finds:
    print(1 if search(to_find) else 0)

