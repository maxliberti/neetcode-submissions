class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        current = ""
        longest = 0
        for l in range(len(s)):
            current = ""
            hs = set()
            for r in range(l, len(s)):
                if s[r] in hs:
                    break
                else:
                    current += s[r]
                    hs.add(s[r])
                    longest = max(len(current), longest)
        return longest