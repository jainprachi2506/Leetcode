# https://github.com/jainprachi2506/Leetcode/blob/master/2017-09-02/two_sum.py

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        
        while i <= j:
            if nums[i]+nums[j] > target:
                j -= 1
            elif nums[i]+nums[j] < target:
                i += 1
            else:
                return [i+1, j+1]
        
        return [-1, -1]
                