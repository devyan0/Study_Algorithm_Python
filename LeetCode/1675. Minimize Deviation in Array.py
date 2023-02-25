from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n % 2 == 1:
                nums[i] <<= 1

        print(nums)
        return 0


arg = [
    [1, 2, 3, 4]
]

res = Solution().minimumDeviation(*arg)
print(res)