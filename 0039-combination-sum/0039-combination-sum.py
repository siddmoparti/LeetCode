class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur_sum, cur_comb):
            if cur_sum == target:
                res.append(cur_comb.copy())
                return
            
            if cur_sum > target or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                cur_comb.append(candidates[j])
                dfs(j, cur_sum + candidates[j], cur_comb)
                cur_comb.pop()
            
            return
                
        dfs(0, 0, [])
        return res

            