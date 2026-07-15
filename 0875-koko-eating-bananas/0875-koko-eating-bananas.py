class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = float('inf')
        while left <= right:
            mid = (right + left) // 2
            cur_hours = 0
            for i in range(len(piles)):
                cur_hours += math.ceil(piles[i] / mid)
            if cur_hours <= h:
                right = mid - 1
                k = mid
            else:
                left = mid + 1
        
        return k
        

