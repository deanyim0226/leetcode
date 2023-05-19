class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        # we can use backtracking algorithm to find all possible combinations 
        # store each possible combination into a new array
        # return the sum of new array
        # time complexity of this algorithm is o( 2^n) where n is the size of nums

        ans = []

        def backtracking(start,currentBitwise):

            ans.append(currentBitwise)

            for i in range(start,len(nums)):
           
                backtracking(i+1,nums[i]^currentBitwise)
      
        backtracking(0,0)

        return sum(ans)