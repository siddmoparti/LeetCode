# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def find_start(node, subNode):
            if not node:
                return False
            if dfs(node, subNode):
                return True
            return find_start(node.left, subNode) or find_start(node.right, subNode)

        def dfs(node, subNode):
            if not node and not subNode:
                return True
            if not subNode:
                return False
            if not node:
                return False
            
            if node.val == subNode.val:
                return dfs(node.left, subNode.left) and dfs(node.right, subNode.right)
            

        return find_start(root, subRoot)
            
            
            
            