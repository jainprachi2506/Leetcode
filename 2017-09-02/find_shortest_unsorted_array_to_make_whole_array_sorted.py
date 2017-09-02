# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        
        if nums == sorted_nums:
            return 0
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            if nums[start] == sorted_nums[start] and nums[end] == sorted_nums[end]:
                start += 1
                end -= 1
            elif nums[start] == sorted_nums[start] and nums[end] != sorted_nums[end]:
                start += 1
            elif nums[start] != sorted_nums[start] and nums[end] == sorted_nums[end]:
                end -= 1
            else:
                return end-start+1
            
        