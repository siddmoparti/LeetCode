class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        self.cur_comb = set()
        def dfs(cur, index):
            if tuple(cur) in self.cur_comb:
                return
            res.append(cur.copy())
            self.cur_comb.add(tuple(cur))
            
            if index >= len(nums):
                return

            for i in range(index, len(nums)):
                cur.append(nums[i])
             
                dfs(cur, i + 1)
                
                cur.pop()

            return
        
        dfs([], 0)
        return res