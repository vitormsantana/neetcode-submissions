# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.IsOkay = True
        self.DFS(root)

        return self.IsOkay
        
    def DFS(self, root):
        if root is None:
            return 0
        
        left_size = self.DFS(root.left)
        right_size = self.DFS(root.right)

        biggest = max(left_size, right_size)
        smallest = min(left_size, right_size)

        if biggest - smallest > 1:
            self.IsOkay = False

        return 1 + biggest