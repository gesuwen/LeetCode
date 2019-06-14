# Linked List, Two Pointers

# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        # get the middle element
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # reverse the first half of the linked list
        p1 = None
        p2 = head
        while p2 != slow:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

        # odd number case
        if fast != None:
            slow = slow.next

        # check first half and second half
        while p1 != None and slow != None:
            if p1.val != slow.val:
                return False
            p1 = p1.next
            slow = slow.next
        return True
