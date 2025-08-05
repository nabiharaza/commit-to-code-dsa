// Last updated: 8/5/2025, 2:56:13 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isUnivalTree(TreeNode root) {
        if (root == null)
            return true;
        return ((root.left == null || root.left.val == root.val && isUnivalTree(root.left)) && 
                (root.right== null || root.right.val== root.val && isUnivalTree(root.right)));
    }
}