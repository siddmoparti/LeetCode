# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node,p,q):
            if not node:
                return None
            if node == p:
                return node
            if node == q:
                return node
            
            right = dfs(node.right,p,q)
            left = dfs(node.left,p,q)
            
            if right and left:
                return node
            elif right:
                return right
            else:
                return left

        return dfs(root,p,q)