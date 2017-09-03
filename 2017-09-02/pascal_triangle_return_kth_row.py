# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return None
        
        if rowIndex == 0:
            return [1]
            
        if rowIndex == 1:
            return [1, 1]
            
        prev = [1, 1]
        i = 2
        while i <= rowIndex:
            new = [1]
            j = 0
            while j < len(prev)-1:
                new.append(prev[j]+prev[j+1])
                j += 1
            new.append(1)
            prev = new
            i += 1
        
        return new
         
        