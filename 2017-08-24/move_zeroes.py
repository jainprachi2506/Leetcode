# https://leetcode.com/problems/move-zeroes/description/
class Solution(object):
    def moveZeroes(self, nums):
        
        # count number of zeros
        i = 0
        j = 1
        
        while j < len(nums):
            if nums[i] != 0:
                i += 1
                j += 1
            else:
                if nums[j] != 0:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    i += 1
                    j += 1
                else:
                    j += 1