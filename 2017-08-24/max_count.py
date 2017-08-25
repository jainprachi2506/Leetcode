# https://leetcode.com/problems/range-addition-ii/description/
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        mmin = nmin = 99999999
        for op in ops:
            mmin = min(mmin, op[0])
            nmin = min(nmin, op[1])
            
        return mmin*nmin
        