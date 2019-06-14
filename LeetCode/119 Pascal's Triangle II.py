# Array

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 3
# Output: [1,3,3,1]
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
from operator import add

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        currentRow = [1]
        for i in range(0, rowIndex):
            currentRow = list( map(add, [0]+currentRow, currentRow+[0]))
        return currentRow
        
