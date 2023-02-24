class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = {0: 0}

        for i in range(1, amount + 1):
            min_coins = float('inf')
            for coin in coins:
                if coin <= i:
                    min_coins = min(min_coins, dp[i - coin] + 1)
            dp[i] = min_coins
        if amount not in dp:
            return -1
        else:
            return dp[amount]