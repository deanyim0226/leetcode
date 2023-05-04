class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        count = 0
        # iterate each row in grid and use binary search to find the first element in each row that is less than 0 
        # as elements are sorted, all elements after the first element will also be negative
        # when binary search is done, we calculate the number of negative elements  
        # The time complexity of this algorithm takes o(m log(n)) where n is the length of row in grid
        # since for m rows, takes o(m) and for each row of matrix we perform a binary search which takes o(logn) 
        # The time complexity is the time to run the algorithm with respect to the size of input

        for row in grid:

            left = 0 
            right = len(row)-1

            while left <= right:

                mid = (left + right) // 2

                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid -1
            
            count += (len(row)- left)

        return count 

        # as elements are sorted in non increasing order both row and column  
        # we can iterate from the bottom of 2d array such that array of the number of rows and 0
        # from the bottom, if we find the element is negative, then we know that all elements after the first element also be negative
        # we can decrease the number of rows by 1
        # if the element is positive, then we increase col by 1 to check whether the element is negative or not 

        # The time complexity of this algorithm takes o(m + n) where m is the number of rows and n is the number of cols
         
        row = len(grid)
        bottom = row-1
        col = 0
        while bottom != -1 and col < len(grid[0]):

            if grid[bottom][col] < 0:
                bottom -= 1

                count += len(grid[0]) - col
            else:
                col += 1

        return count

        # brute force
        col = len(grid[0])
        for i in range(row):
            for j in range(col):

                if grid[i][j] < 0:
                    count += 1
        
        return count