#first try to think to solve with sliding windows but it takes too much for loops so change to dp.

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res =0
        len1 = len(nums1)
        len2 = len(nums2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = 1+ dp[i][j]
                    res = max(res,dp[i+1][j+1])
        return res
