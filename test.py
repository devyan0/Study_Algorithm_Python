class Solution:
    def findValidSplit(self, nums) -> int:
        from math import gcd
        from functools import reduce

        for i, n in enumerate(nums):
            d = 2
            while d < n:
                if n % d != 0:
                    d += 1
                    continue
                while n % d == 0:
                    n = n // d
                n *= d
                d += 1

            nums[i] = n

        prod = reduce(lambda x, y: x * y, nums)
        left = 1

        for i, n in enumerate(nums):
            left = left * n
            prod = prod // n
            if gcd(left, prod) == 1:
                return i

            if i == len(nums) - 2: return -1


res = Solution().findValidSplit([4,7,15,8,3,5])