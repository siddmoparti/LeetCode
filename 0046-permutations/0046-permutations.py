class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                cur.append(nums[i])
                used.add(nums[i])
                dfs(cur)
                used.remove(nums[i])
                cur.pop()
        dfs([])
        return res
       