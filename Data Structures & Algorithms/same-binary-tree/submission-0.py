# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.nodes = []
        self.DFS(p)
        self.DFS(q)

        print(f'primeira metade: {self.nodes[:len(self.nodes)//2]}')
        print(f'segunda metade: {self.nodes[len(self.nodes)//2:]}')

        return self.nodes[:len(self.nodes)//2] == self.nodes[len(self.nodes)//2:] 

    def DFS(self, root):
        if root is None:
            self.nodes.append('')
            return
        
        self.DFS(root.left)
        self.DFS(root.right)
        self.nodes.append(root.val)
        return


        