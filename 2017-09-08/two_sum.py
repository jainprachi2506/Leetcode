# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []
        
        track = {}
        for i in xrange(len(nums)):
            if nums[i] in track:
                return [track[nums[i]], i]
            else:
                track[target-nums[i]] = i
                
        return []