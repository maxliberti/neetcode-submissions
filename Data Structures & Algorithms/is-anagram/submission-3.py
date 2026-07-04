class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countFreqS = {}
        countFreqT = {}

        for char in s:
            lowerChar = char.lower()
            countFreqS[lowerChar] = countFreqS.get(lowerChar, 0) + 1

        for char in t:
            lowerChar = char.lower()
            countFreqT[lowerChar] = countFreqT.get(lowerChar, 0) + 1

        return countFreqS == countFreqT
            
        
