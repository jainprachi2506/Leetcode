# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = deque()
        ret = []
        if root is None:
            return ret
        
        queue.append((1, root))
        while queue:
            level, popped = queue.popleft()
            if len(ret) < level:
                ret.append([])
            ret[-1].append(popped.val)
            
            if popped.left:
                queue.append((level+1, popped.left))
            if popped.right:
                queue.append((level+1, popped.right))
                
        avg = []
        for r in ret:
            avg.append(sum(r)/float(len(r)))
            
        return avg
        
            
        
            
            
    