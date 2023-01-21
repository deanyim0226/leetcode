def maximumUniqueSubarray(nums: list[int]) -> int:

    # This problem can be solved by using two pointers, left and right and using set to keep track of the unique elements
    # right pointer incremented by 1 until we found the dulpicate element
    # we also need to keep track of the sum of the subarray until then 
    # when we found the dulpicate element, we move left pointer until the duplicate element is removed in the set,
    # meaning that we also need to delete the element as left pointer moves and update the currentSum
    # The time complexity of this problem is o(2n) = o(n) since we iterate each list element at most two times

    tempSet = set()

    left = 0
    right = 0

    currSum = 0
    maxSum = 0

    while right < len(nums):
        
        if nums[right] in tempSet:
            while nums[left] != nums[right]:
                tempSet.discard(nums[left])
                currSum -= nums[left]
                left += 1
                
            
            if nums[left] == nums[right]:
                tempSet.discard(nums[left])
                currSum -= nums[left]
                left +=1
                
        else:
            tempSet.add(nums[right])
            currSum += nums[right]
            right += 1

        maxSum = max(maxSum,currSum)

    return maxSum
