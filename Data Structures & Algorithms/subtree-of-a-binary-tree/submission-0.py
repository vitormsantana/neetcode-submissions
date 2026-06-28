# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.nodes = ''
        self.nodes_subtree = ''

        self.DFS(subRoot, True)
        self.DFS(root, False)

        return self.nodes_subtree in self.nodes

    def DFS(self, root, is_subtree):
        if root is None:
            if is_subtree:
                self.nodes_subtree += '-'
                self.nodes_subtree += ('+')
            else:
                self.nodes += '-'
                self.nodes += ('+')
            return
        
        if is_subtree:
            self.nodes_subtree += '-'
            self.nodes_subtree += str(root.val)
        else:
            self.nodes += '-'
            self.nodes += str(root.val)

        self.DFS(root.left, is_subtree)
        self.DFS(root.right, is_subtree)

        return