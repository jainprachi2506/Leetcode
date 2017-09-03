# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        track = {}
        ret = 0
        for n in nums:
            if n in track:
                track[n] += 1
            else:
                track[n] = 1
        
        for key, val in track.iteritems():
            if (k > 0 and key-k in track) or (k == 0 and val > 1):
                ret += 1
                
        return ret
        
        
            
            