# https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 0:
            return False
        
        track = {}
        for n in nums:
            if n not in track:
                track[n] = 1
            else:
                return True
        return False