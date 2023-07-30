# https://leetcode.com/problems/longest-consecutive-sequence/submissions/

#code:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
           return 0
        
        nums = set(nums)
        longest =0
        for num in nums:
            if num-1 not in nums:
                current_num =num
                current =1

                while (current_num+1 in nums):
                    current +=1
                    current_num+=1
                longest = max(current,longest)


        return longest
