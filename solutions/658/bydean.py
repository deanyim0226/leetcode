class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # initial approach was by using binary search algorithm to find the x
        # once we find the value, we perform sliding window algorithm to find the values
        # that satisfied with constraints
        # since the array is sorted, we can use binary search algorithm to find the answer
        # if the element at arr[mid] is closer to x than arr[mid+k], every element to the right of arr[mid+k] can never be the answer
        
        left = 0
        right = len(arr)- 1

        while left <= right:

            mid = (left + right) // 2

            if mid+k < len(arr) and abs(x - arr[mid]) >  abs(x - arr[mid+k]):
                left = mid + 1
            else:
                right = mid - 1
    
        return arr[left:left+k]
       
    
                        