class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedNums = sorted(nums)

        currLongest = 1
        maxLongest = 1
        for i in range(len(nums)):
            if sortedNums[i] == sortedNums[i - 1] + 1: 
                currLongest += 1
                maxLongest = max(maxLongest, currLongest)
            elif sortedNums[i] == sortedNums[i - 1]:
                pass 
            elif sortedNums[i] != sortedNums[i - 1] + 1 and sortedNums[i] != sortedNums[i - 1]:
                currLongest = 1
        return maxLongest