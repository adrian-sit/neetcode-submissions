# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        max_diameter = 0
        while stack:
            node = stack.pop()
            d = self.maxDepth(node.left) + self.maxDepth(node.right)
            max_diameter = max(d, max_diameter)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return max_diameter

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)