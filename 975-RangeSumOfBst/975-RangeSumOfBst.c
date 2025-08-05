// Last updated: 8/5/2025, 2:56:23 PM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int sum;
int rangeSumBST(struct TreeNode* root, int low, int high){
    sum = 0;
    dfssearch(root, low, high); 
    return sum;
}

void dfssearch(struct TreeNode* root, int low, int high) {
    if (root != NULL) {
        if (root->val >= low && root->val <= high) {
            sum += root->val;
        }
        if (low < root->val) {
            dfssearch(root->left, low, high);
        }
        if (high > root->val) {
            dfssearch(root->right, low, high);
        }
    }
}