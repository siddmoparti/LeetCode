from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = right
        while left <= right:
            mid = (left + right) // 2
            current = 0
            for i in range(len(piles)):
                current += math.ceil(piles[i] / mid)
             
            if current <= h:
                right = mid - 1
                best = min(best, mid)
            else:
                left = mid + 1
            
        return best

        