class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = set()
        def dfs(cur, prev):
            if len(cur) >= len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in prev:
                    continue
                cur.append(nums[i])
                prev.add(nums[i])
                dfs(cur, prev)
                prev.remove(nums[i])
                cur.pop()
            return

    
        dfs([], prev)
        return res
        