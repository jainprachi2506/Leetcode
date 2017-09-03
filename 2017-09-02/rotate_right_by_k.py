# https://leetcode.com/problems/rotate-array/description/

class Solution(object):
    def rotate_helper(self, nums, start, end):
        while start < end:
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp
            start += 1
            end -= 1
    
    def rotate(self, nums, k):
        k = k % len(nums)
        if k < 0:
            k = k + len(nums)
        self.rotate_helper(nums, 0, len(nums)-1)
        self.rotate_helper(nums, 0, k-1)
        self.rotate_helper(nums, k, len(nums)-1)