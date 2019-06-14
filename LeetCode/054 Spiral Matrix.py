# Array

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def extractLayer(remain):
            output = []
            matLen, matWid = len(remain), len(remain[0])
            output += remain[0]
            if matLen > 1:
                for i in range(1, matLen):
                    output.append(remain[i][-1])
                if matWid > 1:
                    output += remain[-1][:-1][::-1]
                    for i in range(matLen-2, 0, -1):
                        output.append(remain[i][0])
            return output

        output = []
        remain = matrix[:]
        while len(remain) > 0 and len(remain[0]) > 0:
            output += extractLayer(remain)
            remain = remain[1:-1]
            for row in remain:
                del row[0]
                if len(row) > 0:
                    del row[-1]
        return output

        
