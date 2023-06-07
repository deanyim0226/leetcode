class Solution:
    def climbStairs(self, n: int) -> int:


        # using recursion with memoization
        
        memo = {}
        def helper(step):
            
            if step in memo:
                return memo[step]

            if step == n:
                way = 1
            elif step > n:
                way = 0
            else:
                way = helper(step+1) + helper(step+2)
            
            memo[step] = way
            return way

        helper(0)
        return helper(0)

        # using bottom-up dynamic programming
        
        stair = {}
        stair[1] = 1
        stair[2] = 2

        for i in range(3,n+1):
            
            step = stair[i-1] + stair[i-2]
            stair[i] = step
        
        return stair[n]

        # using recursion
        def helper(step):

            if step == n:
                return 1
            elif step > n:
                return 0
            else:
                return helper(step+1) + helper(step+2)
            
        

        return helper(0)