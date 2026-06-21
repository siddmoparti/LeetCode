class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        index = {}
        for i in range(len(nums)):
            if nums[i] not in index:
                index[nums[i]] = []
            index[nums[i]].append(i)

        for lists in index.values():
            if len(lists) > 1:
                right = 1
                left = 0
                while right < len(lists):
                    if lists[right] - lists[left] <= k:
                        return True
                    else:
                        left += 1
                        right += 1

        return False
