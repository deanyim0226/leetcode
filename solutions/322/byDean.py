class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        # Each index of the array represents an integer amount 
        # dp[index] represents the number of coins that we need to make up that amount
        # we also calculate the fewest number of coins and save it to the corresponding index
        # The time complexity of this problem would be o(n * m) 
        # where n is the given integer,amount and m is the length of the given array(coins) 
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1,len(dp)):
            for element in coins:
                
                remainCoin = i - element

                if remainCoin == 0:
                    dp[i] = 1
                elif remainCoin > 0:
                    dp[i] = min(dp[i],1 + dp[remainCoin])

        if float('inf') == dp[amount]:
            return -1
        else:
            return dp[amount]
     
         
    

        
        


