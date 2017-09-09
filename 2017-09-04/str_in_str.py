# https://leetcode.com/problems/implement-strstr/description/

class Solution(object):
    def strStr(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        find s2 in s1
        """
        # for i in range(len(s1)-len(s2)+1):
        #     if s1[i:i+len(s2)] == s2:
        #         return i
        # return -1
        if len(s2) > len(s1):
            return -1
        if len(s1) == 0 or len(s2) == 0:
            return 0
        
        indexes = []
        for i in xrange(len(s1)):
            if s2[0] == s1[i]:
                indexes.append(i)
                        
        for i in indexes:
            if s1[i:(i+len(s2))] == s2:
                return i
        return -1
                
            
                
                
                
            
        