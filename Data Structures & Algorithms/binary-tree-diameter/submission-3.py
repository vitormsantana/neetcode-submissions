# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxx = 0
        _ = self.DFS(root, self.maxx)

        return  self.maxx

    def DFS(self, root, maxx):
        if root is None:
            return 0
        
        left_side = self.DFS(root.left, self.maxx)
        right_side = self.DFS(root.right, self.maxx)

        self.maxx = max(self.maxx, left_side + right_side)

        return 1 + max(left_side, right_side)