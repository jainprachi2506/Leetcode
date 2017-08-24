# https://leetcode.com/problems/max-consecutive-ones/description/
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1s = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
                if count > max_1s:
                    max_1s = count
            else:
                count = 0
        
        return max_1s