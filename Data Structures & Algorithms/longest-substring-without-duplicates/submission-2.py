class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l = 0
        longest = 0
        for r, c in enumerate(s):
            if c in m:
                l = max(m[c] + 1, l)
            m[c] = r
            longest = max(longest, r - l + 1)

        return longest