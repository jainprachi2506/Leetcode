# https://leetcode.com/problems/keyboard-row/description/

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = set('qwertyuiop')
        r2 = set('asdfghjkl')
        r3 = set('zxcvbnm')
        
        ret = []
        for w in words:
            r = set(w.lower())
            if r == r&r1 or r == r&r2 or r == r&r3:
                ret.append(w)
                
        return ret