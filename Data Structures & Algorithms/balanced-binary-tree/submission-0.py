# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer = True

        def dfs(node):
            if node is None:
                return 0

            #print(f'dfs(node.left): {dfs(node.left)}')
            #print(f'dfs(node.right): {dfs(node.right)}')
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            print(f'node.val: {node.val}')
            print(f'left_height: {left_height}')
            print(f'right_height: {right_height}')
            print(f'abs(left_height - right_height): {abs(left_height - right_height)}')
            if abs(left_height - right_height) > 1:
                self.answer = False
            print(f'self.answer: {self.answer}')
            print('---')

            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.answer