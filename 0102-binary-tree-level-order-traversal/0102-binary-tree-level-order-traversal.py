# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        q = deque()
        q.append(root)

        while q:
            len_q = len(q)
            cur_level = []
            for i in range(len_q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        
        return res

         