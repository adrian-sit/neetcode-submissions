# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        interval = [float('-inf'), float('inf')]

        def dfs(node, interval):

            if node.val <= interval[0] or node.val >= interval[1]:
                return False

            a, b = True, True
            if node.left:
                new_interval = interval.copy()
                new_interval[1] = node.val
                a = dfs(node.left, new_interval)
            if node.right:
                new_interval = interval.copy()
                new_interval[0] = node.val
                b = dfs(node.right, new_interval)
            return a and b

        return dfs(root, interval)