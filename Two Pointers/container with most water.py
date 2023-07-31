#https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        volumes = set()

        i =0 
        j = len(height)-1

        while i<j:
            vol = min(height[i],height[j]) * (j -i)
            volumes.add(vol)

            if height[i]>height[j]:
                j -=1
            elif height[j]>height[i]:
                i+=1
            else:
                 i+=1
        
        return max(volumes)
