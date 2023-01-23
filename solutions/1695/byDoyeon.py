class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        lst = collections.deque()
        l = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] in lst:
                while nums[i] != lst[0]:
                    lst.popleft()
                lst.popleft()
                lst.append(nums[i])
            else:
                lst.append(nums[i])
                res = max(res, sum(lst))
        return res
