class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # We need two dictionaries to verify whether the substring of s is an anagram of p 
        # dictP contains the frequency of each char in P
        # dictS also contains the frequency of each char in S, and we compare two dictionaries whenever
        # the length of dictS is equal to dictP
        # if the length is the same, and two dictionaries have the same key and value, we append the left pointer containing  the index into the list
        # otherwise, we move the left pointer by 1 and keep checking whether it's an anagram or not each iteration 
        # until the left pointer index is greater than the length(len(s)-len(p))   
        # Time complexity of this problem is o(2n) = o(n)

        left = 0
        right = 0
        size = len(p)

        dictS = dict()
        dictP = dict()

        ans = []

        for element in p:
            if element in dictP:
                dictP[element] += 1
            else:
                dictP[element] = 1
        
        for element in s:

            if left == len(s)-size+1:
                break

            if element in dictS:
                dictS[element] += 1
            else:
                dictS[element] = 1
            
            right += 1

            if right == len(p):

                if dictP == dictS:
                    ans.append(left)
                
                if dictS[s[left]] == 1:
                    del dictS[s[left]]
                else:
                    dictS[s[left]] -= 1

                left += 1
                right -=1
            
        return ans

        


        