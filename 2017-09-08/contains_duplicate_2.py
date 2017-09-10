# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        
        track = {}
        for i in xrange(len(nums)):
            if nums[i] not in track:
                track[nums[i]] = [i]
            else:
                for e in track[nums[i]]:
                    if abs(e-i) <= k:
                        return True
                track[nums[i]].append(i)
        
        return False
            
                        
            