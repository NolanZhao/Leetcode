/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        else return isSym(root->left, root->right);
    }
    
    bool isSym(TreeNode *lr, TreeNode *rr) {
        if(!lr && !rr) return true;
        if (lr && rr && lr->val == rr->val){
            return isSym(lr->left, rr->right) && isSym(lr->right, rr->left);
        }
        return false;
    }
};