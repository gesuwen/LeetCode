# Tree

# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        output = []
        def DFS(node, depth=0):
            if node:
                if len(output) <= depth:
                    output.append([0,0])
                output[depth][0] += node.val
                output[depth][1] += 1
                DFS(node.left, depth+1)
                DFS(node.right, depth+1)

        DFS(root)
        return [s/float(c) for s, c in output]
                
