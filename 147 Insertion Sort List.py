# Sort a linked list using insertion sort.
#
# Algorithm of Insertion Sort:
#
# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

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
