class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if mid == left and mid == right:
                return nums[mid]
            if nums[left] <= nums[mid]:
                if nums[left] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[right] < nums[left]:
                    right = mid
                else:
                    left = mid + 1
        return nums[left]
        
        
        
            

        
                