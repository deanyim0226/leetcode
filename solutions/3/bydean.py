def lengthOfLongestSubstring(s: str) -> int:

    #initial approach to this problem would be using dictionary with associated indexes of string  
    #if so, we can easily detect the duplicate character with o(1) time complexity
    #whenever we found the repeating characters, we can calculate the length of the substring.
    #the time complexity of this problem is o(n) since we iterate the string one time
    
    longestLength = 0
    prev = 0
    dic = dict()

    for curr, element in enumerate(s):

        if element in dic: #the case where we find the duplicate character
            prev = max(prev, dic[element]+1)
        
        dic[element] = curr #to indicate current index
        longestLength = max(longestLength, curr-prev+1)

    return longestLength
