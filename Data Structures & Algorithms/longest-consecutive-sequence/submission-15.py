class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = sorted(nums)
        if len(nums) < 2: 
            return len(nums)
        longest = 0

        for i in range(1, len(nums)):
            current = []
            current.append(nums[i - 1])
            for j in range(i, len(nums)):
                if nums[j - 1] == nums[j] - 1:
                    current.append(nums[j])
                else:
                    break
            if len(current) > longest:
                longest = len(current)
        return longest
