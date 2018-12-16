# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.mirror(root.left,root.right)
    
    def mirror(self,root1,root2):
        if root1 == None or root2 == None:
            return root1 == root2
        if root1.val == root2.val:
            return self.mirror(root1.left,root2.right) and self.mirror(root1.right,root2.left)
        else:
            return False