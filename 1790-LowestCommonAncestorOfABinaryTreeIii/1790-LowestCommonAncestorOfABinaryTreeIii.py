# Last updated: 8/5/2025, 2:53:05 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents_node_p = set()
        
        node = p
        while node:
            parents_node_p.add(node.val)
            node = node.parent
        
        node = q
        while node and not node.val in parents_node_p:
            node = node.parent
        
        return node
        