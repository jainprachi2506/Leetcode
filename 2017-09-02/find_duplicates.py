# https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        track = {}
        
        for n in nums:
            if n in track:
                return True
            else:
                track[n] = 1
                
        return False