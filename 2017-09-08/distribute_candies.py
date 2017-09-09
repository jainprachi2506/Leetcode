# https://leetcode.com/problems/distribute-candies/description/

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(candies) == 0:
            return 0
        
        track = {}
        for c in candies:
            if c in track:
                track[c] += 1
            else:
                track[c] = 1
        
        return min(len(candies)/2, len(track))
        