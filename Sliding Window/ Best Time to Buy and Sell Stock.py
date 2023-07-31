# LINK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

#code:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 
        right = 0+1
        highest=0

        while right < len(prices):
            if(prices[left] >= prices[right]):
                left= right
                right+=1
            
            else:
                profit = prices[right] - prices[left]
                if profit >= highest:
                    highest = profit
                right+=1
        
        return highest

        
        #HIGH TIME COMPLEXITY
        # answers = set()
        
        # maximum = max(prices)
        # index = prices.index(maximum)

        # for i ,n in enumerate(prices):
        #     if n < maximum and i<index:
        #         ans = maximum - n
        #         answers.add(ans)
            
        #     else:
        #         sublist = prices[i+1:]
        #         if not sublist:  # Check if sublist is empty
        #             continue  
        #         maximum = max(sublist)
        #         index = prices.index(maximum)
        #         ans = maximum - n
        #         answers.add(ans)
        
        # if not answers:  # Check if answers set is empty
        #     return 0

        # if max(answers) <= 0:
        #     return 0
        
        # else:
        #     return max(answers)