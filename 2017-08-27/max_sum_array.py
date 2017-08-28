# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def create_structure(self, nums):
        dp = nums
        for i in xrange(1, len(nums)):
            dp[i] = max(dp[i], dp[i]+dp[i-1])
        return dp
            
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = self.create_structure(nums)
        max_sum = dp[0]
        for i in xrange(1, len(dp)):
            if dp[i] > max_sum:
                max_sum = dp[i]
                
        return max_sum