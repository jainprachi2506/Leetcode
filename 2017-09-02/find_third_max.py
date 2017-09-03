# https://leetcode.com/problems/third-maximum-number/description/

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        first = second = third = float('-inf')
        
        for n in nums:
            if n > first:
                first = n
        
        if len(nums) >= 3:
            for n in nums:
                if n > second and n < first:
                    second = n
            
            for n in nums:
                if n > third and n < second:
                    third = n
                    
            return third
        return first

                
        
            