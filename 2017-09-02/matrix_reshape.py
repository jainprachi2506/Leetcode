# https://leetcode.com/problems/reshape-the-matrix/description/

class Solution(object):
    def matrixReshape(self, old_nums, new_rows, new_cols):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        old_rows = len(old_nums)
        old_cols = len(old_nums[0])
        
        if old_rows*old_cols != new_rows*new_cols:
            return old_nums
        
        new_nums = [] 
        new_row = []
        
        for old_i in xrange(old_rows):
            for old_j in xrange(old_cols):
                new_row.append(old_nums[old_i][old_j])
                if len(new_row) == new_cols:
                    new_nums.append(new_row)
                    new_row = []
                    
        return new_nums
