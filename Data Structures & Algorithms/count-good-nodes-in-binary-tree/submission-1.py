# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        self.DFS(root, -float('inf'))

        return self.good

    def DFS(self, root, maxx):
        if root is None:
            return None

        if root.val >= maxx:
            print(f'iremos aumentar good em 1, pois root.val {root.val} >= maxx {maxx}')
            self.good += 1
            maxx = root.val

        _ = self.DFS(root.left, maxx)
        _ = self.DFS(root.right, maxx)

        return 0

        
        
