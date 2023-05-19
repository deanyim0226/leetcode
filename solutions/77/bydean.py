class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # return k size of all possible combinations in the range from 1 to n
        # iterate from 1 to n
        # whenever list reached to the size of k 
        # we add it to the ans list and backtrack 

        def helper(index, curr, ans):

            if len(curr) == k:
             
                ans.append(curr[:])
                return
            else:

                for i in range(index, n+1):

                    curr.append(i)
                    helper(i+1, curr,ans)
                    curr.pop()
            
        
        ans = []
        helper(1,[],ans)

        return ans
        