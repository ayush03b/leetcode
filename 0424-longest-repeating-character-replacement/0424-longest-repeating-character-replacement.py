class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        res = L = 0
        for R in range(len(s)):
            counter[s[R]] = counter.get(s[R], 0) + 1
            while (R - L + 1) - max(counter.values()) > k:
                counter[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res