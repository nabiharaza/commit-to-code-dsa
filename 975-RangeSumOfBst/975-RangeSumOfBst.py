# Last updated: 8/5/2025, 2:56:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        path = []

        def rangeSumBSTHelper(root, L, R, path):
            if root is None:
                return
            if root.val >= L and root.val <= R:
                path.append(root.val)

            rangeSumBSTHelper(root.left, L, R, path)
            rangeSumBSTHelper(root.right, L, R, path)

        rangeSumBSTHelper(root, L, R, path)
        print(sum(path))
        return sum(path)