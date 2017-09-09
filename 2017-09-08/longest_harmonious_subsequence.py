# https://leetcode.com/problems/longest-harmonious-subsequence/description/

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        
        track = {}
        
        for n in nums:
            if n in track:
                track[n] += 1
            else:
                track[n] = 1
        
        max_len = 0
        for k, v in track.iteritems():
            if k+1 in track:
                max_len = max(max_len, track[k]+track[k+1])
        return max_len
                
            