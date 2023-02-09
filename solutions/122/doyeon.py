class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > l:
                res += prices[i] -l
                l = prices[i]
            else:
                l = prices[i]
        return res
