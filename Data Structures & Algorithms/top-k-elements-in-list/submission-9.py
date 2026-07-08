import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqBucket = {}
        for num in nums:
            freqBucket[num] = freqBucket.get(num, 0) + 1

        arr = []
        for key, value in freqBucket.items():
            arr.append([value,key])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res