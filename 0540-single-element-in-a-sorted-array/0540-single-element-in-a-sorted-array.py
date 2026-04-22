class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid
            elif mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid
        
        return nums[left]

        #check if even or odd index:
        #if odd, check if number left to is same and if not the issue is on the left side
        #if even, check if number to its right is the same and if not the issue is on the left side