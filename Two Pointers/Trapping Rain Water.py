# https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        answer = [0] * len(height)
        left_min = height[left]
        right_min = height[right]

        while left<right:
            if left_min < right_min or left_min == right_min:
                left+=1
                if left_min - height[left] <0 or left_min - height[left] ==0:
                    answer[left] = 0
                else:
                    answer[left] = left_min - height[left]
                
                if height[left] > left_min:
                    left_min = height[left]
            else:
                right-=1

                if right_min - height[right] <0 or right_min - height[right] ==0:
                    answer[right] = 0
                else:
                    answer[right] = right_min - height[right]
                
                if height[right] > right_min:
                    right_min = height[right]
            
        
        return sum(answer)
