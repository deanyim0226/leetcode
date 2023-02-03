class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        num_check = ''
        for n in nums1:
            num_check += chr(n)

        check = ''
        answer = 0
        for i in nums2:
            check += chr(i)
            print(check) 
            if check in num_check:
                answer = max(len(check), answer)
            else:
                check = check[1:]

        return answer