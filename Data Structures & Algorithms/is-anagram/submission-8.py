class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freqS, freqT = {}, {}
        for char in s:
            freqS[char] = freqS.get(char, 0) + 1
        for char in t:
            freqT[char] = freqT.get(char, 0) + 1

        for key in freqS.keys():
            if key not in freqT:
                return False
            elif freqS[key] != freqT[key]:
                return False
        return True


