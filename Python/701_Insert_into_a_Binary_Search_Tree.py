# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if root.val < val:
            node = self.insertIntoBST(root.right, val)
            root.right = node
        if root.val > val:
            node = self.insertIntoBST(root.left, val)
            root.left = node

        return root