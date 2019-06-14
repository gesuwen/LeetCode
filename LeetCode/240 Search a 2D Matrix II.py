# Binary Search; Divide and conquer

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                L, R = 0, col-1
                while L <= R:
                    mid = (L+R)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        R = mid - 1
                    else:
                        L = mid + 1
        for j in range(col):
            if target >= matrix[0][j] and target <= matrix[-1][j]:
                L, R = 0, row-1
                while L <= R:
                    mid = (L+R)//2
                    if matrix[mid][j] == target:
                        return True
                    elif matrix[mid][j] > target:
                        R = mid - 1
                    else:
                        L = mid + 1
        return False
