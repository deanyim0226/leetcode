class Solution:
    def findMin(self, nums: List[int]) -> int:

        # compare index 0 of array to index -1 of array to check whether the array is rotated or not
        # we perform the binary search algorithm to look for the value satisfied with the condition where
        # nums[mid] is less than nums[mid+1] or nums[mid-1] is greater than nums[mid]
        # if nums[mid] is greater than nums[left], the value we are looking for is located on the right side of mid
        # if not, the value is located on the left side of mid

        # the time complexity of this algorithm takes o(logn) 

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums)-1

        if nums[0] < nums[right]:
            return nums[0]

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            

            if nums[mid-1] > nums[mid]:
                return nums[mid]


            if nums[left] <= nums[mid]:
                left = mid +1
            else:
                right = mid -1
            

        return -1