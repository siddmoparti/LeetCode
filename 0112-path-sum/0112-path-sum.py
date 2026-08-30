# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, cur_sum):
            if not node:
                return False
            cur_sum += node.val
            if cur_sum == targetSum and not(node.right or node.left):
                return True
            
            left = dfs(node.left, cur_sum)
            right = dfs(node.right, cur_sum)

            return left or right
        
        return dfs(root, 0)
            

            
        