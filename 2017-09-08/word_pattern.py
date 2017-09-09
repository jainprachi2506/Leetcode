# https://leetcode.com/problems/word-pattern/description/

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        
        if len(pattern) != len(str):
            return False
        
        track = {}
        seen = []
        for i in xrange(len(pattern)):
            if pattern[i] not in track and str[i] not in seen:
                track[pattern[i]] = str[i]
                seen.append(str[i])
            elif (pattern[i] not in track and str[i] in seen) or track[pattern[i]] != str[i] :
                return False
        return True