class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = []
        end = []
        c = capacity
        min_heap = []
        for ppl,starting,ending in trips:
            start.append([starting,ppl])
            end.append([ending, -1 * ppl])
    
        for starting, ppl in start:
            heapq.heappush(min_heap, (starting,ppl))
        for ending, ppl in end:
            heapq.heappush(min_heap, (ending, ppl))
        
        while c >= 0 and min_heap:
            time, ppl = heapq.heappop(min_heap)
            c -= ppl
            if c < 0:
                return False
        
        return True
            
            

            
            
        
