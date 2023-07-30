#Link: https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        start =1
        for i in range(len(nums)):
            res[i] = start
            start = nums[i]*start

        end =1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*end
            end = nums[i]*end
        
        return res
