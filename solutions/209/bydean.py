import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    
    # need two pointers for iterating the whole array and subarray 
    # iterate the array and calculate the sum of each element 
    # if the sum is greater than equal to target, calculate the length of subarray 
    # we keep doing this until the condition fails
    # time complexity of this algorithm is o(n) where n is the size of array 

        ptr = 0

        minLength = math.inf
        total = 0


        for i in range(len(nums)):

            total += nums[i]

            while total >= target:
                
                minLength = min(minLength, i - ptr + 1)
                total -= nums[ptr]
                ptr += 1

        
        if minLength == math.inf:
            return 0
        else:
            return minLength


