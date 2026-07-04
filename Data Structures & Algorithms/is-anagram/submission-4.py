class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countFreqS = {}
        countFreqT = {}

        for char in s:
            countFreqS[char] = countFreqS.get(char, 0) + 1

        for char in t:
            countFreqT[char] = countFreqT.get(char, 0) + 1

        return countFreqS == countFreqT
            
        
