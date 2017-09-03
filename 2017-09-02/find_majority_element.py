# https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        track = {}
        
        for n in nums:
            if n in track:
                track[n] += 1
            else:
                track[n] = 1
        
        for k, v in track.iteritems():
            if v > math.floor(len(nums)/2):
                return k
            
        return None