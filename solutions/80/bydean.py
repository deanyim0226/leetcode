class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # it is okay to have two duplicates, but it needs to be removed when we have more than 2 dulicates

        # we can solve this problem by using a pointer that keeps track of inserting position
        # need a variable to count the number of duplicates. we are only interested in finding duplicates at most twice
        # We don't consider count variable after 2. Otherwise, we modify the array so that we can have at most two duplicates

        # time complexity of this algorithm is o(n) where n is the size of nums array

        count = 1
        insertPointer = 1
        
        for i in range(1,len(nums)):
        
            if nums[i] == nums[i-1]:

                if count < 2:
                    nums[insertPointer] = nums[i]
                    insertPointer += 1

                count += 1

            else:
                nums[insertPointer] = nums[i]
                insertPointer += 1
                count = 1

        difference = len(nums) - insertPointer

        while difference != 0:
            nums.pop()
            difference -= 1

        return insertPointer