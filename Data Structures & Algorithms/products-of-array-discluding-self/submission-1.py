import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = math.prod(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                el = product // nums[i]
                res.append(el)
            else:
                prod = 1
                for j in range(len(nums)):
                    if j != i:
                        prod *= nums[j]
                res.append(prod)
        return res