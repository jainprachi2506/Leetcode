# https://leetcode.com/problems/arithmetic-slices/description/

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2:
            return 0
        
        c = s = 0
        for i in xrange(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                c += 1
                s += c
            else:
                c = 0
                
        return s