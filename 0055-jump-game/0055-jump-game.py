class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = n - 1
        goal = n - 1

        while i > 0:
            if nums[i - 1] + (i - 1) >= goal:
                goal = i - 1
            i -= 1

        return goal == 0