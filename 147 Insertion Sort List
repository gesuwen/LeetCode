# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = ListNode(-1)
        curr = temp
        while head:
            # check if it is needed to reset the curr pointer
            if curr and curr.val > head.val:
                curr = temp
            # find the place to insert
            while curr.next and curr.next.val < head.val:
                curr = curr.next
            # insert and sort the next element
            curr.next, curr.next.next, head = head, curr.next, head.next
        return temp.next
