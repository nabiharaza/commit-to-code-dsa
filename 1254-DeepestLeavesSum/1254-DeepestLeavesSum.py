# Last updated: 8/5/2025, 2:54:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        total = 0

        def dfs(root, depth):
            nonlocal max_depth, total
            if not root:
                return
        
            if not root.left and not root.right:
                if depth > max_depth:
                    total = root.val
                    max_depth = depth
                elif depth == max_depth:
                    total += root.val
            else:
                dfs(root.left, depth+1)
                dfs(root.right, depth+1)
            
            return


        dfs(root, 0)

        return total

