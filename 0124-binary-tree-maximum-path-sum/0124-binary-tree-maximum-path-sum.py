class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # path passing through this node
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # path going upward to parent
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]