class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # it's obvious to find the element that appears exactly once by iterating the array 
        
        # use binary search algorithm to find the element that appears once.
        # when we perform the binary search, we get the mid index
        # we compare the values that appear left and right
        # the value we are looking for is located on the odd lengthed side 

        # The time complexity of this algorithm takes o(logn) where n is the size of list

        left = 0 
        right = len(nums)-1

        while left <= right:
            
            mid = (left + right) // 2

            isEven = (right - mid) % 2 == 0

            if mid-1 > -1 and nums[mid] == nums[mid-1]:
                
                if isEven:
                    right = mid - 2
                else:
                    left = mid + 1
            elif mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                if isEven:
                    left = mid + 2
                else:
                    right = mid - 1
            else:
                return nums[mid]
    
        return nums[left]