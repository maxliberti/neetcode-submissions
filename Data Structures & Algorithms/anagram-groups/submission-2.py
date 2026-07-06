from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            if str(sorted(s)) in res.keys():
                for key in res.keys():
                    if key == str(sorted(s)):
                        res[key].append(s)
            else:
                res[str(sorted(s))].append(s)
        return list(res.values())
