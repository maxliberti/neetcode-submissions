import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqBucket = {}
        for num in nums:
            freqBucket[num] = freqBucket.get(num, 0) + 1

        freqList = []
        for key, value in freqBucket.items():
            freqList.append([value, key])

        res = []
        heapq.heapify_max(freqList)
        for i in range(k):
            res.append(heapq.heappop_max(freqList)[1])
        return res