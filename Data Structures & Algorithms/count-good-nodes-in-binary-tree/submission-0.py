# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        array_with_good_nodes = []

        def dfs(node, array_with_good_nodes, maxx):
            if node is None:
                return
            
            if node.val >= maxx:
                array_with_good_nodes.append(node.val)
                maxx = node.val
            
            if node.left:
                dfs(node.left, array_with_good_nodes, maxx)
            
            if node.right:
                dfs(node.right, array_with_good_nodes, maxx)

            return len(array_with_good_nodes)
        
        return dfs(root, array_with_good_nodes, -float('inf'))