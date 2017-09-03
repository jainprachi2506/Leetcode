# https://leetcode.com/problems/pascals-triangle/description/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        ret = [[1], [1, 1]]
        
        for i in xrange(2, numRows):
            last = ret[-1]
            temp = [1]
            i = 0
            while i < len(last)-1:
                temp.append(last[i]+last[i+1])
                i += 1
            temp.append(1)
            ret.append(temp)
        return ret
        
        
                    
                