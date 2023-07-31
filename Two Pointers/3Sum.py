# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        ans= []

        for i ,num in enumerate(nums):
            if i>0 and nums[i-1] == num:
                continue
            j = i+1
            k = len(nums)-1

            while j<k:
                answer = num + nums[j] + nums[k]

                if answer > 0:
                    k-=1
                elif answer < 0:
                    j+=1      
                else:
                    ans.append([num , nums[j], nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        
        return ans