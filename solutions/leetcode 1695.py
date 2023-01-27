class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = []
        answer = 0
        for i in nums:
            if i not in check:
                check.append(i)
            else:
                new_start = check.index(i) + 1
                check = check[new_start:] + [i]

            answer = max(sum(check), answer) 

        return answer