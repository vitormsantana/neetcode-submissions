# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        result = []
        self.answer = True

        def dfs(node):
            if node is None:
                return
            
            if node.left:
                dfs(node.left)
            
            if len(result) > 0:
                if node.val <= result[-1]:
                    print(f'node.val: {node.val}')
                    print(f'result[-1]: {result[-1]}')
                    self.answer = False

            result.append(node.val)

            if node.right:
                dfs(node.right)
            
            return self.answer

        return dfs(root)