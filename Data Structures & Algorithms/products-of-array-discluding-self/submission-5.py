class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        # make list where each element is the product of everything to the left of the element at the same index in nums
        pre = 1
        for i in range(len(nums)):
            res.append(pre)
            pre *= nums[i]
        
        # multiply each element by the product of everything to the right of the element at the same index in nums
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res