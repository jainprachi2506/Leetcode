# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLength(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
        
            
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        ll_len = self.getLength(head)
        
        current = head
        i = 0
        while i < (ll_len+1)//2:
            current = current.next
            i += 1
        
        rev_head = current
        prev = None
        
        while rev_head:
            current = rev_head
            rev_head = current.next
            current.next = prev
            prev = current
            
        while head and prev:
            if head.val == prev.val:
                head = head.next
                prev = prev.next
            else:
                return False
            
        return True
        
            
        
        
        
        
        
        