# https://leetcode.com/problems/non-decreasing-array/discuss/

class Solution(object):
    def valid(self, nums):
        for i in xrange(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True
        
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one = nums[:]
        two = nums[:]
        
        for i in xrange(len(nums)-1):
            if nums[i] > nums[i+1]:
                one[i] = nums[i+1]
                two[i+1] = nums[i]
                break
        
        return self.valid(one) or self.valid(two)
                
                