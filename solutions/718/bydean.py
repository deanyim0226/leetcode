class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #initially we create a 2d array filled with 0
        #whenever we encounter the same element, it's a subarray that appears in both arrays
        #we keep track of the same element and add the previous element
        #time complexity would be o(n*m) where n is length of nums1, m is length of nums2
        
        length = 0
        #col * row
        grid = [[0]* len(nums2)] * len(nums1)
        
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):

                if nums1[i] == nums2[j]:
                    if i-1 >= 0 and j-1 >= 0: 
                        grid[i][j] = 1 + grid[i-1][j-1]
                    else:
                        grid[i][j] = 1

                length = max(length,grid[i][j])

        return length