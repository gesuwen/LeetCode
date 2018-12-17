# Math

# You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.
#
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation:
# The five points are show in the figure below. The red triangle is the largest.
#
#
# Notes:
#
# 3 <= points.length <= 50.
# No points will be duplicated.
#  -50 <= points[i][j] <= 50.
# Answers within 10^-6 of the true value will be accepted as correct.

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def triArea(point1, point2, point3):
            x1, y1, x2, y2, x3, y3, = point1[0], point1[1], point2[0], point2[1], point3[0], point3[1]
            return 1/2 * abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)

        comb = itertools.combinations(points, 3)
        output = 0
        for p1, p2, p3 in comb:
            output = max(output, triArea(p1, p2, p3))
        return output
        
