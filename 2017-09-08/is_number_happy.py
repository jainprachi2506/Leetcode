# https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        track = {1}
        while n not in track:
            track.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1
            
                
            