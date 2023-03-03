from typing import List


class Solution:
    def __init__(self):
        self.base = 3

    def strStr(self, haystack: str, needle: str) -> int:
        self.n = n = len(needle)
        m = len(haystack)
        if m < n: return -1
        cnt = 0
        key = self.custom_hash(needle, 0, n - 1)
        cmp = self.custom_hash(haystack, 0, n - 1)
        start = 0
        while start + n < m:
            if key == cmp: return start
            cmp = self.custom_shift(cmp, haystack[start], haystack[start + n])
            start += 1
        return -1 if key != cmp else start

    def custom_shift(self, hash_val, out, come):
        return ((hash_val - ord(out)) // self.base) + ord(come) * (self.base ** (self.n - 1))

    def custom_hash(self, s, start, end):
        hash_val = 0
        for i in range(start, end + 1):
            hash_val += ord(s[i]) * (self.base ** (i - start))

        return hash_val


arg = [
    "ababcaababcaabc", "ababcaabc",

]

res = Solution().strStr(*arg)
print(res)