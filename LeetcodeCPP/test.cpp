#include <iostream>
#include <vector>
using  namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};



class Solution {
public:
    TreeNode *sortedArrayToBST(vector<int> &num) {
        return arrayToBST(num, 0, num.size()-1);
    }
    
    TreeNode *arrayToBST(vector<int> &num, int start, int end){
        if (start > end) return NULL;
        int mid = start + ()
    }






}


