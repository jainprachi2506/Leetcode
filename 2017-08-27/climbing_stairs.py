# https://leetcode.com/problems/climbing-stairs/description/

class Solution(object):
    def create_structure(self, n, dp):
        for i in xrange(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
            
        return dp
            
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fixed = [0, 1, 2]
        
        if n <= 2:
            return fixed[n]
        
        dp = self.create_structure(n, fixed)
                        
        return dp[-1]