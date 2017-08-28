# https://leetcode.com/problems/unique-binary-search-trees/description/

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        
        for node in xrange(2, n+1):
            for root_node in xrange(1, node+1):
                left = root_node-1
                right = node-root_node
                
                dp[node] = dp[node] + (dp[left]*dp[right])
                
        return dp[n]
                