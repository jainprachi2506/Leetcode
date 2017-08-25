# https://leetcode.com/problems/find-the-difference/description/
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        track = {}
        
        for c in s:
            if c not in track:
                track[c] = 1
            else:
                track[c] += 1
                
        for c in t:
            if c not in track or track[c] <= 0:
                return c
            else:
                track[c] -= 1
                
        return ''