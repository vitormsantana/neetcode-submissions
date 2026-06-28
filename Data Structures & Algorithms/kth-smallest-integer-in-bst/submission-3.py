# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        self.answer = -1000
        self.k = k
        self.DFS(root)

        return self.answer

    def DFS(self, root):
        if root is None:
            return
        
        self.DFS(root.left)
        self.nodes.append(root.val)
        if self.k == len(self.nodes):
            self.answer = self.nodes[-1]
            # print(f'updating self.answer para {self.answer}')
        # else:
            # print(f'k: {self.k}')
            # print(f'len(self.nodes): {len(self.nodes)}')
            # print(f'self.nodes: {self.nodes}')
            # print('---')
        self.DFS(root.right)

        return 0