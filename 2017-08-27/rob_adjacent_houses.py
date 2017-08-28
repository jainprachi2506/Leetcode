# https://leetcode.com/problems/house-robber/description/

class Solution(object):
    def create_structure(self, nums):
        dp = nums
        dp[1] = max(dp[0], dp[1])
        for i in xrange(2, len(nums)):
            dp[i] = max(dp[i]+dp[i-2], dp[i-1])
        
        return dp     
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp = self.create_structure(nums)
        
        max_amt = dp[0]
        for i in xrange(1, len(dp)):
            if dp[i] > max_amt:
                max_amt = dp[i]
                
        return max_amt
        