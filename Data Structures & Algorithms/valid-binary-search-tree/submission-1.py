# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.DFS(root, -float('inf'), float('inf'))

    def DFS(self, root, minn, maxx):
        if root is None:
            return True

        if root.val >= maxx or root.val <= minn:
            return False
        
        return self.DFS(root.left, minn, root.val) and self.DFS(root.right, root.val, maxx)