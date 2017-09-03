# https://leetcode.com/problems/search-insert-position/description/

class Solution(object):
    def searchInsertBinary(self, start, end, nums, target):
        if start > end:
            return start
        
        mid = start + ((end-start)//2)
        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            return self.searchInsertBinary(start, mid-1, nums, target)
        else:
            return self.searchInsertBinary(mid+1, end, nums, target)
        
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.searchInsertBinary(0, len(nums)-1, nums, target)
        
    
        
        
        
        
        
        