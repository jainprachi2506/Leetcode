# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]: [1, 2, 9]
        :rtype: List[int]:       [1, 3, 0]
        
        """
        ret = []
        
        i = len(digits)-1
        
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
        
        if i >= 0:
            digits[i] += 1
        else:
            digits = [1] + digits
        
        return digits
        
        
            
        
        