# Last updated: 8/5/2025, 2:56:38 PM
class Solution:
    def leafSimilar(self, root1, root2):
        
        def dfs(root, res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
                return
            
            dfs(root.left,  res)
            dfs(root.right, res)
            return

        if not root1 or not root2:
            return False

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2    
# class Solution:
#     def leafSimilar(self, root1, root2):
        # def dfs(node):
        #     if node:
        #         if not node.left and not node.right:
        #             yield node.val
        #         yield from dfs(node.left)
        #         yield from dfs(node.right)

        # return list(dfs(root1)) == list(dfs(root2))        
        # def modified_dfs(root) -> list:
        #     if not root:
        #         return []
        #     if not root.left and not root.right:
        #         return [root.val]
            
        #     return modified_dfs(root.left) + modified_dfs(root.right)


        # list1 = modified_dfs(root1)
        # list2 = modified_dfs(root2)

        # return list1 == list2


        # def custom_dfs(root) -> list:
        #     leaf_nodes = []
        #     stack = []
        #     stack.append(root)

        #     while stack:
        #         curr = stack.pop()
        #         if not curr.left and not curr.right: # leaf node
        #             leaf_nodes.append(curr.val)
        #         else:
        #             if curr.right:
        #                 stack.append(curr.right)
        #             if curr.left:
        #                 stack.append(curr.left)
            
        #     return leaf_nodes

        # # print(custom_dfs(root1))
        # # print(custom_dfs(root2))
        # return True if custom_dfs(root1) == custom_dfs(root2) else False





# For root1
# DFS traverse the tree
# Check for the leafnode is basically just if its child is null
# Leaf nodes [6 7 4 9 8] -> store this result

# For root2
# DFS traverse the tree
# Check for the leafnode is basically just if its child is null
# Leaf nodes [6 7 4 9 8] -> store this result

# compare the lists
# return an output











