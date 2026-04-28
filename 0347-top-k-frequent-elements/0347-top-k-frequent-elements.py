class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)
        count = Counter(nums)
        # 1 : 3
        # 2 : 2
        # 3 : 1
        for key,value in count.items():
            heapq.heappush(minHeap, [value,key])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for value, key in minHeap:
            res.append(key)
        
        return res