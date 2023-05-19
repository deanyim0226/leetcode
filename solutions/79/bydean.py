class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
   
        # use DFS and backtracking
        # time complexity of this algorithm is o(n * 3^m)
        # where n is the number of cells, m is the length of the word
        
        grid = [ [False for i in range(len(board[0])) ] for j in range(len(board))]

        def backtracking(grid,row,col,word,index):
            
            if index == len(word):
                return True
            else:
                
                if row < 0 or row == len(board) or col < 0 or col == len(board[0]) or board[row][col] != word[index]:
                    return False

                if grid[row][col] == False:
                    grid[row][col] = True
                else:
                    return False
        
                for rowOffset , colOffset in [(0,1), (0,-1), (1,0), (-1,0)]:
                    
                    if backtracking(grid,row+rowOffset, col+colOffset, word, index+1):
                        return True
                    
                grid[row][col] = False     
                return False   


        for i in range(len(board)):
            for j in range(len(board[0])):

                if backtracking(grid,i,j,word,0):
                    return True

                
        return False