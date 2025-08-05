# Last updated: 8/5/2025, 2:56:10 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        store = set()
        def traverse(root):
            if root:
                store.add(root.val)
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        if len(store) <= 1:
            return True
        else:
            return False