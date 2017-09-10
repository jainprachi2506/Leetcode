# https://leetcode.com/problems/isomorphic-strings/description/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        track = {}
        visited = []
        for i in xrange(len(s)):
            if s[i] not in track:
                if t[i] not in visited:
                    track[s[i]] = t[i]
                    visited.append(t[i])
                else:
                    return False
            elif track[s[i]] != t[i]:
                return False
        return True
            