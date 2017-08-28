# https://leetcode.com/problems/continuous-subarray-sum/description/

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # n = len(nums)
        # for i in xrange(0, n):
        #     s = nums[i]
        #     for j in xrange(i+1, n):
        #         s += nums[j]
        #         if k == 0 and s == 0:
        #             return True
        #         if k!= 0 and s % k == 0:
        #             return True
        # return False
        if k == 0:
            return len(nums) >= 2 and nums[0] == 0 and nums[1] == 0
        k = abs(k)
        dp = {}
        s = 0
        for i, n in enumerate(nums):
            s = (s+n)%k
            if s == 0 and i > 0:
                return True
            if s in dp and i-dp[s] >= 2:
                return True
            if s not in dp:
                dp[s] = i
                    
        return False
            
            