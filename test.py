from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        res = 0
        cnt = Counter()

        while r < len(s):
            in_ = s[r]

            while cnt[in_] > 0:
                out_ = s[l]
                cnt[out_] -= 1
                l += 1

            cnt[in_] += 1
            r += 1

            res = max(res, r - l)

        return res


sol = Solution()
res = sol.lengthOfLongestSubstring("abcabcbb")
print(res)