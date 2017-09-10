# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        
        ret = []
        track = {}
        for n in nums1:
            if n not in track:
                track[n] = 1
        
        for n in nums2:
            if n in track and n not in ret:
                ret.append(n)
                
        return ret
                
                