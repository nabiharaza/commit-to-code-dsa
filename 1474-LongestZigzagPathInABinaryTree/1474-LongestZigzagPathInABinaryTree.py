# Last updated: 8/5/2025, 2:54:11 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # self.pathLength = 0
        
        # def dfs(node, goLeft, steps):
        #     if node:
        #         self.pathLength = max(self.pathLength, steps)
        #         if goLeft:
        #             dfs(node.left, False, steps + 1)
        #             dfs(node.right, True, 1)
        #         else:
        #             dfs(node.left, False, 1)
        #             dfs(node.right, True, steps + 1)

        # dfs(root, True, 0)
        # return self.pathLength


        def dfs(root, dir, maxPath):
            if not root:
                return 0
            maxLeft, maxRight = 0,0
            if root.left:
                if (dir == 'r' or not dir):
                    maxLeft =  max(maxPath, dfs(root.left, 'l', maxPath+1))
                else:
                    maxLeft = dfs(root.left, 'l', 1)
            if root.right:
                if (dir == 'l' or not dir):
                    maxRight = max(maxPath, dfs(root.right, 'r', maxPath+1))
                else:
                    maxRight = dfs(root.right, 'r', 1)
            return max(maxPath, maxRight, maxLeft)
        
        return dfs(root, '', 0)