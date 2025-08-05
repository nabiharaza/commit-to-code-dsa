// Last updated: 8/5/2025, 2:54:04 PM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int goodNodes(TreeNode* root) {
       return depth_first_search(root, std::numeric_limits<int>::min());
    }

private:
    int depth_first_search(TreeNode* root, int curr_max) {
        if (!root) {
            return 0;
        }

        int count = 0;
        if (curr_max <= root->val) {
            // Node is good.
            count ++;
            curr_max = root->val;
        }

        count += depth_first_search(root->left, curr_max);
        count += depth_first_search(root->right, curr_max);

        return count;
    }
};