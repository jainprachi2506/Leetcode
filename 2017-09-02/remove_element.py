# https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        if not nums:
            return 0
        
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                
                j -= 1
            else:
                i += 1
        
        return i
        
        
                
            
                

                
                
                
        