class Solution:
    def rob(self, nums: List[int]) -> int:

        # In order to avoid alerting the police, you cannot rob the adjacent houses
        # you need to rob the houses without noticing the police and get the maximum amount of money

        # either we can start index 0 or index 1 
        # you cannot rob the house that is the next to the house that you robbed already

        # use dp
        # time complexity is the time to run algorithm with respect to the size of input
        # for this particular problem, it takes linear time 
        # space complexity is also o(n) 
        memo = {}

        if len(nums) >= 2: 
            memo[0] = nums[0]
            memo[1] = max(nums[0], nums[1])

            for index in range(2,len(nums)):
                
                ans = max(memo[index-1], memo[index-2] + nums[index])
                memo[index] = ans
            return memo[len(nums)-1]
        else:
            return nums[0]
            

        # use recursion + memoization  
        # time complexity of this problem is o(n) since we are calling the function n times 
        # space complexity is o(n)
        memo = {}

        def recursion(index):
            
            if index > len(nums)-1:
                return 0 
            
            if index in memo:
                return memo[index]

            ans = max(recursion(index+1), recursion(index+2) + nums[index])
            memo[index] = ans

            return ans
      
        return recursion(0)

        # use recursion to find the maximum amount of money
        # time complexity of this problem is o(2^n) and space complextity is o(n) since we are using stack to call recursive funtion 
        def recursion(index):

            if index > len(nums)-1:
                return 0
            else:
                return max(recursion(index+1) , recursion(index+2) + nums[index])
        

        return recursion(0)