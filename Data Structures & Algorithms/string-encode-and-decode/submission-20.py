class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "@" + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        i = 0
        while i < len(s):
            if s[i] in nums:
                length = ""
                while s[i] != "@":
                    length += s[i]
                    i += 1 
                length = int(length)
                word = ""
                for j in range(length):
                    i += 1
                    word += s[i]
                i += 1   
                res.append(word)
        return res
