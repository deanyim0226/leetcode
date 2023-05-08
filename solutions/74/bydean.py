class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # think of the 2d array as 1d array 
        # we need to calculcate the position to access the 2d array as a 1d array
        # 1 3 5 7 10 11 16 20 23 30 34 60

        # imagine that we access 1d array of 5 which is 11 
        # in 2d array, we can access the value 11 with 1,1 index of 2d array
        # which is bascially 5 // len(matrix[0]) for row and 5 % len(matrix[0]) for col
        
        # we perform the binary search algorithm based on this condition to find the target value
        # The time complextity of this algorithm is o(lon(m * n)) where m is the size of col and n is the size of row

        while left <= right:

            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid -1
            
        return False
             