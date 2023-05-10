class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        # suppose we have an array containing numbers from 1 to the len(arr)
        # given sorted array we are interested in finding a kth element from missing values in the given array
        # we know the number of missing values by comparing each each element in two arrays 
        # if the number of missing values are less than k, we iterate it until we find the number of missing values is greater k

        # 1 2 3 4 5
        # 2 3 4 7 11, k = 5

        # the time complexity of this algorithm is o(Log(n))


        left = 0
        right = len(arr)-1
     
        while left <= right:

            mid = (left + right) // 2

            numberOfMissingValue = arr[mid] - mid - 1
     
            if numberOfMissingValue < k: 
                left = mid + 1
            else:
                right = mid - 1

        numOfmissingValue = arr[right] - right - 1
        
        return arr[right] + k  - numOfmissingValue

        # 2 3 4 7 11
        # arr[i+1] - arr[i] -1 represents the number of missing values in between arr[i+1] and arr[i]
        
        # if arr[0] is not 1 then we know that there is at least one missing value
        # iterate the array and keep track of missing value
        # if the number of missing value is less than k, we substract the value by missing value
        # if the number of missing value is greater than k, we know that there is missing value in that range

        # the time complexity of this algorithm is o(n)

        if k <= arr[0] - 1:
            return k
        
        k -= arr[0]-  1

        for i in range(len(arr)-1):

            missingValue = arr[i+1] - arr[i] - 1

            if k <= missingValue:
                return arr[i] + k

            k -= missingValue

        return arr[-1] + k


        # I'm going to find the missing positive integers 
        # since the elements of the array is sorted, if the last element of the array is not equal to the size of index, 
        # we know that there are missing values
        # if it is then we know that missing values are listed after the last element of the array

        # the time complexity of this algorithm is o(n^2)
        
        lastElement = arr[-1]

        if lastElement == len(arr):
            
            ans = lastElement
            return ans + k

        else:

            missingArray = []

            for i in range(1,lastElement+k):           
                missingArray.append(i)

            for element in arr:
                missingArray.remove(element)

            return missingArray[k-1]


            

            
                
                


                


        

    