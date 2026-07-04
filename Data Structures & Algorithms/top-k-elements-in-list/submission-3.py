class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = {}
        res = []

        for i in range(len(nums)):
            countFreq[nums[i]] = countFreq.get(nums[i], 0) + 1

        for i in range(k):
            topKey = max(countFreq, key=countFreq.get)
            res.append(topKey)
            del countFreq[topKey]
        
        return res
        