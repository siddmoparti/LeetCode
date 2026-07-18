class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(nums) + 2):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i - 2])

        #[0,0,1,2,4,4]
        
        return dp[-1]