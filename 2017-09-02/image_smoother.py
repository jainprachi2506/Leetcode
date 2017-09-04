# https://leetcode.com/problems/image-smoother/description/

import math
class Solution(object):
    def getAverage(self, I, J, M):
        averageSum = 0;
        averageCount = 0;
        for i in xrange(max(0, I-1), min(I+2, len(M))):
            for j in xrange(max(0, J-1), min(J+2, len(M[0]))):
                averageSum += M[i][j]
                averageCount += 1
        return int(math.floor(averageSum/averageCount))
                
                
            
        
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        for i in xrange(len(M)):
            ret.append([])
            l = ret[-1]
            for j in xrange(len(M[0])):
                l.append(self.getAverage(i, j, M))
        return ret
        
                
        