# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        t = root.left
        root.left = root.right
        root.right = t
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
