class Solution:   
    # starting from the end, we need to figure out whether goal is reachable or not
    # if we can jump from the previous index to the goal, then the goal is reachable from the previous index
    # we iterate it until we find the answer
    # the time complexity would be o(n) where n is the length of nums

    def canJump(self, nums: List[int]) -> bool:
     
        if len(nums) < 2:
            return True

        goal = len(nums)-1
        curr = len(nums)-2

        while goal != 0:
            jump = nums[curr]

            if jump + curr >= goal:
                goal = curr

            if goal == curr and curr == 0:
                return True
            
            curr -=1

            if curr < 0:
                return False

      
 