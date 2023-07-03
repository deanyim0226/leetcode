class Solution:
    def removeDuplicates(self, nums: List[int]) :
        """
        1 3 3 6 7 7 9
        1 3 6 7 9

        I am going to use the ptr1 equal to zero, then access the index of the array nums using loops
        i need while loop and if statement to commpare if the first element of array smaller than second one if it is true i will keep the first one if it is not true i will remove that element in the array 
    and i commpare if it is the same number or not if it is i will remove it using method remove.

        """

        ptr1 = 0
        ptr2 = len(nums)-1

        while ptr1 < ptr2:
            
            if nums[ptr1] < nums[ptr1+1]:
                
                ptr1 = ptr1 + 1
        
            else:
                nums.remove(nums[ptr1])
                ptr2 = len(nums)-1
                
            

        return len(nums)


           



