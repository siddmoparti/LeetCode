class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        cur_sum = 0
        res = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            if (cur_sum - k) in prefix:
                res += prefix[cur_sum-k]
            prefix[cur_sum] = prefix.get(cur_sum, 0) + 1
        
        return res
        
            
