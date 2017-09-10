# https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for n in nums:
            ret = ret ^ n
            
        return ret
                