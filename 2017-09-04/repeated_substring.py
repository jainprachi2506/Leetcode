# https://leetcode.com/problems/repeated-substring-pattern/description/

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if len(str) < 2:
            return False
        
        len_str = len(str)
        for i in xrange(1, (len_str//2)+1):
            rem = len_str % i
            if rem == 0:
                s = str[:i]
                if s*(len_str//i) == str:
                    return True
        return False
            
            
            
            
            