# https://leetcode.com/problems/construct-the-rectangle/description/
import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        ret = []
        i = 1
        min_diff = area
        mid = int(math.sqrt(area))
        
        while i <= mid:
            if area % i == 0:
                diff = (area//i)-i
                if diff < min_diff:
                    min_diff = diff
                    ret = [area//i, i]
            i += 1
                
        return ret