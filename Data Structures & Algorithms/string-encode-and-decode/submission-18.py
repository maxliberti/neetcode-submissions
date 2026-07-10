class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "@" + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        left = 0
        right = 0
        while left < len(s):
            if s[left] in nums:
                length = ""
                while s[right] != "@":
                    length += s[right]
                    right += 1
                length = int(length)
                word = ""
                right += 1
                for i in range(length):
                    word += s[right]
                    right += 1
                res.append(word)
                left = right
            else:
                break
        return res
