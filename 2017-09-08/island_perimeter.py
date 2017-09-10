# https://leetcode.com/problems/island-perimeter/description/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        per = 0
        
        m = len(grid)  # rows
        n = len(grid[0])  # columns
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    per_to_add = 4
                    if i > 0 and grid[i-1][j] == 1:
                        per_to_add -= 1
                    if j > 0 and grid[i][j-1] == 1:
                        per_to_add -= 1
                    if i < m-1 and grid[i+1][j] == 1:
                        per_to_add -= 1
                    if j < n-1 and grid[i][j+1] == 1:
                        per_to_add -= 1
                    
                    per += per_to_add
            
        return per
                
                    
                            
                    
                    