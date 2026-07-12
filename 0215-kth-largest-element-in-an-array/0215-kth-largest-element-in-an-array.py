import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)
        for i in range(len(nums)):
            heapq.heappush(minHeap, nums[i])
        
        
        
        for i in range(len(nums) - k):
            heapq.heappop(minHeap)
        
        res = heapq.heappop(minHeap)
        return res
        

        
        


            