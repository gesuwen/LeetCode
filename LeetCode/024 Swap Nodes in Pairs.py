# Linked list

# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:
#
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr, curr.next = self, head
        while curr.next and curr.next.next:
            a = curr.next
            b = a.next
            curr.next, b.next, a.next = b, a, b.next
            curr = a
        return self.next
