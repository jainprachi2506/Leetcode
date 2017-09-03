# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        
        if not nums:
            return ret
        
        for i, v in enumerate(nums):
            nums[abs(v)-1] = -1*(abs(nums[abs(v)-1]))
            
        for i, v in enumerate(nums):
            if v > 0:
                ret.append(i+1)
        
        return ret
        