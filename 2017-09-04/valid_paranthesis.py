# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, string):
        """
        :type string: str
        :rtype: bool
        """
        if len(string) == 0:
            return True
        
        brackets_map = {'(':')', '[':']', '{':'}'}
        
        stack = []
        for i in xrange(len(string)):
            if string[i] in brackets_map:
                stack.append(string[i])
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if brackets_map[top] != string[i]:
                        return False
        
        return len(stack) == 0
                