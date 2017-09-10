# https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        track = {}
        
        for c in s:
            if c in track:
                track[c] += 1
            else:
                track[c] = 1
        
        for c in t:
            if c not in track or track[c] < 1:
                return False
            else:
                track[c] -= 1
                
        for key, val in track.iteritems():
            if val != 0:
                return False
        return True