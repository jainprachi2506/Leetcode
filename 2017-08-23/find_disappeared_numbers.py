# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for n in nums:
            if nums[abs(n)-1] > 0:
                nums[abs(n)-1] = (-1)*nums[abs(n)-1]
                        
        for i in xrange(len(nums)):
            if nums[i] > 0:
                ret.append(i+1)
                
        return ret