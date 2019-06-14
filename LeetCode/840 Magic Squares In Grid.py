# array

# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
#
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).
#
#
#
# Example 1:
#
# Input: [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276
#
# while this one is not:
# 384
# 519
# 762
#
# In total, there is only one magic square inside the given grid.
# Note:
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # a b c
        # d e f
        # g h i
        def magic(a,b,c,d,e,f,g,h,i):
            inputList = [a,b,c,d,e,f,g,h,i]
            inputList.sort()
            if a+b+c == d+e+f == g+h+i == a+e+i == c+e+g == a+d+g == b+e+h == c+f+i and [1,2,3,4,5,6,7,8,9] == inputList:

                return True
            return False
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if magic(grid[i][j],grid[i][j+1],grid[i][j+2],
                         grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                         grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]):
                    count += 1
        return count
                
