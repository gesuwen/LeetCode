// Array; Dynamic Programming
//
// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
//
// Note: You can only move either down or right at any point in time.
//
// Example:
//
// Input:
// [
//   [1,3,1],
//   [1,5,1],
//   [4,2,1]
// ]
// Output: 7
// Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution {
    public int minPathSum(int[][] grid) {
        return minCostPath(0, 0, grid.length-1, grid[0].length-1, grid, new int[grid.length + 1][grid[0].length + 1]);
    }

    private static int minCostPath(int sr, int sc, int dr, int dc, int[][] arr, int[][] qb) {
        if (sr == dr && sc == dc) return arr[sr][sc];
        if (sr > dr || sc > dc) return Integer.MAX_VALUE;
        if (qb[sr][sc] != 0) {
            return qb[sr][sc];
        }
        int cstod = 0;
        int cihtod = minCostPath(sr, sc + 1, dr, dc, arr, qb);
        int civtod = minCostPath(sr + 1, sc, dr, dc, arr, qb);
        cstod = arr[sr][sc] + Math.min(cihtod, civtod);
        qb[sr][sc] = cstod;
        return cstod;
    }
}
