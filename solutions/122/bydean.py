class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we just need to add up profit whenever it happens.
        #time complexity of this problem is o(n)
        
        maxProfit = 0

        for i in range(1,len(prices)):
            
            if prices[i] - prices[i-1] > 0:
                maxProfit += prices[i]- prices[i-1]

        return maxProfit  

