# https://leetcode.com/problems/decode-ways/description/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)                
        if n == 0:
            return 0
        dp = [0]*n
        if int(s[-1]) != 0:
            dp[-1] = 1
        
        for i in xrange(n-2, -1, -1):
            if int(s[i]) == 0:
                continue
            dp[i] = dp[i]+dp[i+1]
            if 10 <= int(s[i:i+2]) <= 26:
                if i + 2 >= n:
                    dp[i] = dp[i] + 1
                else:
                    dp[i] = dp[i] + dp[i+2]
                
        return dp[0]