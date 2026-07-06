from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        ordered = sorted(counts.keys(), key=counts.get, reverse=True)
        return ordered[:k]