# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        track = {}
        
        for i, v in enumerate(nums):
            if v not in track:
                track[v] = [i]
            else:
                for e in track[v]:
                    if abs(e-i) <= k:
                        return True
                track[v].append(i)
                
        return False
                        
            