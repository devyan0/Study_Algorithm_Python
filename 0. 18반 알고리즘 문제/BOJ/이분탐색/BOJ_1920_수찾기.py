"""
https://www.acmicpc.net/problem/1920
case 1 -> case 3: parametric search
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

def search(target, nums=nums):
    l, r = 0, len(nums)
    while l < r:
        mid = (l+r)//2
        if target <= nums[mid]:
            r = mid
        else:
            l = mid+1
    return l < len(nums) and nums[l] == target

K = int(input())
finds = map(int, input().split())
for to_find in finds:
    print(1 if search(to_find) else 0)

