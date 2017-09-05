# https://leetcode.com/problems/house-robber/description/

class Solution(object): 
    def create_structure(self, nums):
        self.dp = nums
        self.dp[1] = max(self.dp[0], self.dp[1])
        for i in xrange(2, len(nums)):
            self.dp[i] = max(self.dp[i]+self.dp[i-2], self.dp[i-1])
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        self.create_structure(nums)
        return max(self.dp)