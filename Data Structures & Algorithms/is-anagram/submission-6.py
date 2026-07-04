class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS, freqT = {}, {}
        for char in s:
            freqS[char] = freqS.get(char, 0) + 1
        for char in t:
            freqT[char] = freqT.get(char, 0) + 1

        return freqS == freqT
