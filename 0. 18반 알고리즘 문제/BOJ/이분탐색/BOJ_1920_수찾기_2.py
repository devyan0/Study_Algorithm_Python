"""
https://www.acmicpc.net/problem/1920
case1: 정확히 pin point
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

def search(target, nums=nums):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        check_num = nums[mid]
        if check_num == target:
            return True
        elif check_num < target:
            l = mid + 1
        elif target < check_num:
            r = mid - 1

    return False

K = int(input())
finds = map(int, input().split())
for to_find in finds:
    print(1 if search(to_find) else 0)

