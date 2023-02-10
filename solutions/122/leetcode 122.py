class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pre_val = prices[0]
        result = 0
        for n in prices[1:]:
            if n > pre_val:
                add_val = n - pre_val
                result += add_val
            pre_val = n
        return result