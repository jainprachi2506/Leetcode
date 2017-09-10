# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

class Solution(object):
    def intersect(self, nums1, nums2):
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
            else:
                track[n] += 1
        
        for n in nums2:
            if n in track and track[n] > 0:
                ret.append(n)
                track[n] -= 1
                
        return ret