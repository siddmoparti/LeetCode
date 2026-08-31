# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p:
            return p
        if root == q:
            return q
        

        def dfs(node):
            if not node:
                return None
            if node.val == p.val:
                return p
            if node.val == q.val:
                return q
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            return left or right
        
        left = dfs(root.left)
        right = dfs(root.right)
        
        if left and right:
            return root
        if left and not right:
            return left
        if right and not left:
            return right
        
            