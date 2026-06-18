class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        cur_sum = 0
        res = float('inf')

        while right < len(nums):
            cur_sum += nums[right]
            while cur_sum >= target:
                res = min(right - left + 1, res)
                cur_sum -= nums[left]
                left += 1
            right += 1
        
        if res == float('inf'):
            return 0
        
        return res
            
