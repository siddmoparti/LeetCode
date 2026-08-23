class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur, start):
            res.append(cur.copy())
            
            
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.pop()
            
            return

                

        dfs([], 0)
        return res
                
            


            

            

        
        
        