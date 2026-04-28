from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best = float("inf")

        #[3,6,7,11].  1,2,3,[4,5],6,7,8,9,10,11
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            
            if hours > h:
                l = mid + 1
            elif hours <= h:
                best = min(best, mid)
                r = mid - 1
            
        
        return best

        
       

        