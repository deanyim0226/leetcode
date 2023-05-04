class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        recent_index = 0

        for i, v in enumerate(nums):
            if recent_index < i:
                return False 
            compare_index = i+v
            recent_index = max(recent_index, compare_index)
        return True