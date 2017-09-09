# https://leetcode.com/problems/reverse-string/description/

class Solution(object):
    def reverseString(self, string):
        """
        :type string: str
        :rtype: str
        """
        i = 0
        j = len(string)-1
        string = list(string)
        while i < j:
            temp = string[i]
            string[i] = string[j]
            string[j] = temp
            i += 1
            j -= 1
            
        return ''.join(string)
            