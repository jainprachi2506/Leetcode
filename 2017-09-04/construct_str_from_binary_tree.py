# https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree3strcreate(self, root, ret):
        if root is None:
            return ''
        
        ret.append(str(root.val))
        
        if root.left and root.right:
            ret.append('(')
            self.tree3strcreate(root.left, ret)
            ret.append(')')
            ret.append('(')
            self.tree3strcreate(root.right, ret)
            ret.append(')')
        elif root.right:
            ret.append('(')
            ret.append(')')
            ret.append('(')
            self.tree3strcreate(root.right, ret)
            ret.append(')')
        elif root.left:
            ret.append('(')
            self.tree3strcreate(root.left, ret)
            ret.append(')')
        return ret
        
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        ret = []
        res = self.tree3strcreate(t, ret)
        return ''.join(res)
            
            
        
            
        
            
        
            