# https://leetcode.com/problems/integer-break/description/

class Solution(object):
    def create_structure(self, n):
        return [0]*n
    
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 1
        
        dp = self.create_structure(n+1)
        
        dp[1] = dp[2] = 1
        
        for i in xrange(3, n+1):
            for j in xrange(1, i/2+1):
                temp = max(j, dp[j]) * max(i-j, dp[i-j])
                if temp > dp[i]:
                    dp[i] = temp
                    
        return dp[n]
        