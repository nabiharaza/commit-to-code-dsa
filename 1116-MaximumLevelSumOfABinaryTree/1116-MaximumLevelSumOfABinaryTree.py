# Last updated: 8/5/2025, 2:55:45 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans, level, maxSum = 0, 0, float('-inf')
        q = collections.deque([root])

        while q:
            sumAtCurrentLevel = 0
            level += 1

            for i in range(len(q)):
                node = q.popleft()
                sumAtCurrentLevel += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if maxSum < sumAtCurrentLevel:
                maxSum, ans = sumAtCurrentLevel, level

        return ans

                
            


