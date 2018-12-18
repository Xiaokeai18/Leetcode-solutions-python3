# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tree = []
        opt = []
        layer = 0
        if root != None:
            tree.append([root]) 
        else:
            return []
        while tree[layer]:  #层数变了
            tree.append([]) #新建一层
            for i in tree[layer]:
                if i.left:
                    tree[layer+1].append(i.left)
                if i.right:
                    tree[layer+1].append(i.right)
            layer += 1
        layer = 0
        for i in tree[-2::-1]:
            opt.append([])
            for j in i:
                opt[layer].append(j.val)
            layer += 1
        return opt
