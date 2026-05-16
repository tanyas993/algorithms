# 110
# 110
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_height(self, node):
        if node is None:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def isBalanced(self, root):
        if root is None:
            return True
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        diff = left - right
        if diff < 0:
            diff = -diff
        if diff > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


#572
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def same_trees(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        if tree1.val != tree2.val:
            return False
        return self.same_trees(tree1.left, tree2.left) and self.same_trees(tree1.right, tree2.right)
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        if self.same_trees(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)