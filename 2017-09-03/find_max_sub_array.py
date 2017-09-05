# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def create_structure(self, nums):
        self.dp = nums
        for i in xrange(1, len(nums)):
            self.dp[i] = max(self.dp[i], self.dp[i]+self.dp[i-1])
            
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.create_structure(nums)
        return max(self.dp)