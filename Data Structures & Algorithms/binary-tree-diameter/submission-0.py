# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxx = -float("inf")

        def dfs(node):
            if node is None:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            self.maxx = max(self.maxx, (left_sum + right_sum))

            return 1 + max(left_sum, right_sum)
        
        dfs(root)
        return self.maxx