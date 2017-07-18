# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSym(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSym(p.left, q.right) and self.isSym(p.right, q.left)
        return False


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.isSym(root.left, root.right)
        return True