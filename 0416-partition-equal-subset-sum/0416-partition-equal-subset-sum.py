class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2

        
        cur_set = set()
        cur_set.add(0)
        for i in range(len(nums) - 1, -1, -1):
            temp_set = set()
            for num in cur_set:
                if num + nums[i] not in cur_set:
                    temp_set.add(num + nums[i]) 
            cur_set.update(temp_set)
            
        
        return target in cur_set
        
