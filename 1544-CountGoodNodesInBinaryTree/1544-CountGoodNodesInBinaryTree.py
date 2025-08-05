# Last updated: 8/5/2025, 2:54:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## DFS Iterative
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, prev_max):
            if not root:
                return 0
            
            if root.val >= prev_max:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, prev_max) + dfs(root.right, prev_max)


        return dfs(root, root.val)














        # stack = [(root, float("-inf"))]
        # num_good_nodes = 0
        
        # while stack:
        #     node, max_so_far = stack.pop()
        #     if max_so_far <= node.val:
        #         num_good_nodes += 1
        #     if node.right:
        #         stack.append((node.right, max(node.val, max_so_far)))
        #     if node.left:
        #         stack.append((node.left, max(node.val, max_so_far)))
        
        # return num_good_nodes
        
        # if not root:
        #     return 0
        
        # good_nodes = 0
        # stack = []
        # stack.append((root, root.val))

        # while stack:
        #     curr, maxVal = stack.pop()
        #     if curr.val >= maxVal:
        #         good_nodes += 1
        #         maxVal = curr.val
        #     if curr.right:
        #         stack.append((curr.right, maxVal))
        #     if curr.left:
        #         stack.append((curr.left, maxVal))

        # return good_nodes