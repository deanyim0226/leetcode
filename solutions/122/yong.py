class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        profit = 0
        left = 0
        right = 1

        while left < right and right <len(prices):

            if prices[left] > prices[right]:
                left += 1
                right += 1
            else : 
                profit = profit + prices[right] - prices[left]
                left+=1
                right+=1
        
        return profit
            

            
                
        return profit
