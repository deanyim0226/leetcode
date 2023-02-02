class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        seen = set()
        total = 0 # to see current sum
        score = 0 # to hold the sum of unique elements

        #right is index that keep moving
        #left is index that increment when there is duplicate number in seen
        
        #input = [4,2,4,5,6]
        for right in range(len(nums)): 
            
            print(right)#right = 0, 1, 2, 3, 4

            while nums[right] in seen: 
                # remove the head of element 
                seen.remove(nums[left])
                # subract head of the element
                total -= nums[left]
                # move the left pointer
                left += 1
            #

            #if it is not seen, add to the sum, and seen find max of current window
            # add to the seen
            seen.add(nums[right])
            # 
            total += nums[right]
            #find max between curr score
            score = max(score, total)
        return score
