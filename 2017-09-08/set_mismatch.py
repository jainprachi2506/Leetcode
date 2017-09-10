# https://leetcode.com/problems/set-mismatch/description/

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in xrange(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                ret.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = -1*nums[abs(nums[i])-1]
                
        for i in xrange(len(nums)):
            if nums[i] > 0:
                ret.append(i+1)
        
        return ret