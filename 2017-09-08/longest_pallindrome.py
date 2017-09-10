# https://leetcode.com/problems/longest-palindrome/description/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        
        track = {}
        is_single_included = False
        ret = 0
        for c in s:
            if c in track:
                track[c] += 1
            else:
                track[c] = 1
        
        for k, v in track.iteritems():
            if v % 2 == 0:
                ret += v
            else:
                ret += v-1
                if not is_single_included:
                    ret += 1
                    is_single_included = True
            
        return ret
                
        
        
            
                