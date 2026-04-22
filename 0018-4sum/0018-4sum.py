class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for p in range(i + 1, len(nums)):
                if p > i + 1 and nums[p] == nums[p - 1]:
                    continue
                
                j = p + 1
                k = len(nums) - 1
                while j < k:
                    val = nums[i] + nums[p] + nums[j] + nums[k]
                    if val == target:
                        res.append([nums[i], nums[p], nums[j], nums[k]])
                        j += 1
                        k -= 1

                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    
                    elif val < target:
                        j += 1
                    elif val > target:
                        k -= 1
            
        return res
                    
