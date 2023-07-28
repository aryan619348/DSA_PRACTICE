#https://leetcode.com/problems/top-k-frequent-elements/submissions/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count ={}
        ans =[]
        for n in nums:
            count[n] = count.get(n,0) +1
        
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)


        # Print the first 'n' keys
        for i in range(min(k, len(sorted_items))):
            ans.append(sorted_items[i][0])
        
        return ans
            

