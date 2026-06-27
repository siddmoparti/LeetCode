class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index = -1
        second_index = -1

        # find first index
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                first_index = mid
                right = mid - 1

        if first_index == -1:
            return [-1, -1]

        # find last index, starting after first_index
        second_index = first_index
        left = first_index + 1
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                second_index = mid
                left = mid + 1

        return [first_index, second_index]