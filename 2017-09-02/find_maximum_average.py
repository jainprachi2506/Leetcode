# https://leetcode.com/problems/maximum-average-subarray-i/description/

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) < k:
            return 0.0
        
        temp_sum = 0
        
        for i in xrange(k):
            temp_sum += nums[i]
        
        all_sums = [temp_sum]
        
        start = 0
        end = k
        while end < len(nums):
            all_sums.append(all_sums[-1] - nums[start] + nums[end])
            start += 1
            end += 1
        
        return float(max(all_sums))/float(k)
            
            
        
        