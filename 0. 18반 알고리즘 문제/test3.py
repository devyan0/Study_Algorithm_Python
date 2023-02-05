class Solution:
    def findAnagrams(self, s, p):
        from collections import Counter
        valid = 0
        lookup = Counter(p)
        window = Counter()
        l, r = 0, 0
        res = []
        while r < len(s):
            in_ = s[r]
            r += 1

            if in_ in lookup:
                window[in_] += 1
                if window[in_] == lookup[in_]:
                    valid += 1

            while valid == len(lookup):
                if r - l == len(p):
                    res.append(l)

                out_ = s[l]
                l += 1


                if out_ in lookup:
                    if window[out_] == lookup[out_]:
                        valid -= 1
                    window[out_] -= 1



        return res

res = Solution().findAnagrams("abaacbabc", "abc")
print('res = ', res)