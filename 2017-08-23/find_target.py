# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack = []
        track = ()
        found = False
        if root is None:
            return found
        stack.append(root)
        while stack:
            popped = stack.pop()
            if popped.val not in track:
                track.add(k-popped.val)
            else:
                found = True
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)
                
        return found