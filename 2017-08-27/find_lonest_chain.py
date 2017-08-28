# https://leetcode.com/problems/maximum-length-of-pair-chain/description/

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs) == 0:
            return 0
        
        if len(pairs) == 1:
            return 1
        
        pairs.sort(key=lambda x: x[1])
            
        dp = [1]*len(pairs)
        overall_max = 1
        for i in xrange(1, len(pairs)):
            for j in xrange(i):
                if pairs[i][0] > pairs[j][1]:
                    tmp = dp[j]+1
                    if tmp > dp[i]:
                        dp[i] = tmp
                        
        return max(dp)
        