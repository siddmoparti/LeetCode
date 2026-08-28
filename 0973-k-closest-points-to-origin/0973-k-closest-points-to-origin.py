class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def euclidean(x1,y1,x2,y2):
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        
        min_heap = []
        

        for x,y in points:
            distance = euclidean(x,y,0,0)
            heapq.heappush(min_heap, (distance, x, y))
        res = []

        for i in range(k):
            distance, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        
        return res


        