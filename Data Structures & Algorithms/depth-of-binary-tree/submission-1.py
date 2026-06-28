# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left:
            left_size  = self.maxDepth(root.left)
        else:
            left_size = 0

        if root.right:
            right_size  = self.maxDepth(root.right)
        else:
            right_size = 0

        return max(1 + left_size, 1 + right_size)
