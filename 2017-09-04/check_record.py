# https://leetcode.com/problems/student-attendance-record-i/description/

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) in [0, 1]:
            return True
        
        a = 0
        for i in xrange(len(s)):
            if s[i] == 'A':
                a += 1
                if a > 1:
                    return False
            elif (s[i] == 'L') and (i-1 >= 0 and s[i-1] == 'L') and (i+1 < len(s) and s[i+1] == 'L'):
                return False
            
        return True