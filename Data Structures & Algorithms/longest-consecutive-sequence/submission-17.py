class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        hashset = set(nums)
        longest = 0

        for num in hashset:
            if num - 1 not in hashset:
                current = 1
                while num + current in hashset:
                    current += 1
                if current > longest:
                    longest = current
        return longest
