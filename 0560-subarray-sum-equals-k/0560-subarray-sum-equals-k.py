class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {}
        res = 0
        prefix[0] = 1
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if (curSum - k) in prefix:
                res += prefix[curSum-k]
            prefix[curSum] = 1 + prefix.get(curSum, 0)
        
        return res
