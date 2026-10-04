# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxd = 0
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.height(root.left) + 1, self.height(root.right) + 1)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        d = self.height(root.left) + self.height(root.right)
        self.maxd = max(max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)), d)
        return self.maxd
