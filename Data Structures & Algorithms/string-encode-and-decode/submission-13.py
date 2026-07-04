class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s
            res += "`"
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        string = ""
        for c in s:
            if c != "`":
                string += c
            else:
                res.append(string)
                string = ""
        return res

