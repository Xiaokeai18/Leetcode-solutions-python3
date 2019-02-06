# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            if root.left:
                if self.hasPathSum(root.left,sum-root.val):
                    return True
            if root.right:
                if self.hasPathSum(root.right,sum-root.val):
                    return True
            elif not root.left: #indicates this node is a leaf
                if sum == root.val:
                    return True
        return False

