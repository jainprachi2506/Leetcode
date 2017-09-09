# https://leetcode.com/problems/ransom-note/description/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) == 0 and len(ransomNote) == 0:
            return True
        
        if len(magazine) < len(ransomNote):
            return False
        
        track = {}
        
        for c in magazine:
            if c in track:
                track[c] += 1
            else:
                track[c] = 1
                
        for c in ransomNote:
            if c not in track or track[c] <= 0:
                return False
            else:
                track[c] -= 1
                
        return True
        
            
        