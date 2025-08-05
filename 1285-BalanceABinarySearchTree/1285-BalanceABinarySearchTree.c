// Last updated: 8/5/2025, 2:54:44 PM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void postOrder(struct TreeNode* root, int *count) {
    
    if(root == NULL)
        return;
    
    postOrder(root->left,count);
    postOrder(root->right,count);
    (*count)++;
    
}
//create binaryTreeArray
void binaryTreeArray(struct TreeNode *root, struct TreeNode **returnArray, int *k) {
    
    
    if(root == NULL)
        return;
    
    binaryTreeArray(root->left,returnArray,k);
    
    returnArray[(*k)++] = root;
    binaryTreeArray(root->right,returnArray,k);
}

//convert to balance tree
struct TreeNode* binarySearchTree(struct TreeNode **returnArray, int low, int high) {
    struct TreeNode *temp;
    if(low > high)
        return NULL;
    int mid = (low+high)/2;    
    
    temp = returnArray[mid];
    temp->left = binarySearchTree(returnArray,low,mid-1);
    temp->right = binarySearchTree(returnArray,mid+1,high);
    
    return temp;
    
}

struct TreeNode* balanceBST(struct TreeNode* root){
    
    int count=0;
    int k=0;
    struct TreeNode **returnArray;
    
    //do postOrder
    postOrder(root, &count);

    //create arr of binary search tree
    returnArray = (struct TreeNode **)malloc(sizeof(struct TreeNode*) * count);
    binaryTreeArray(root, returnArray, &k) ;  
    
    //conver
    root = binarySearchTree(returnArray,0,count-1);
    free(returnArray);
    return root;
}