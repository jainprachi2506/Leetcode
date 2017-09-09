# https://leetcode.com/problems/valid-palindrome/description/

class Solution(object):
    def isAlphaNumeric(self, c):
        c_alphanumeric = ord(c)
        if c_alphanumeric >= ord('a') and c_alphanumeric <= ord('z'):
            return True
        if c_alphanumeric >= ord('A') and c_alphanumeric <= ord('Z'):
            return True
        if c_alphanumeric >= ord('0') and c_alphanumeric <= ord('9'):
            return True
        return False
        
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while i <= j:
            if self.isAlphaNumeric(s[i]) and self.isAlphaNumeric(s[j]):
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            else:
                if not self.isAlphaNumeric(s[i]):
                    i += 1
                if not self.isAlphaNumeric(s[j]):
                    j -= 1
                
        return True
                
            
            
        