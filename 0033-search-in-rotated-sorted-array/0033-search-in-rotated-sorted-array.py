class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1,2,3,4] 
        # [3,4,1,2] target = 1 output = 2
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right ) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return -1

        # check if left and right side is sorted
        #is target > middle or target < left
        # on the right side check if target < mid or target > right

