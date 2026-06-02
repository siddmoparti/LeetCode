class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        buckets = [0] * (n+1)

        for c in citations:
            buckets[min(n,c)] += 1
        
        h = n
        papers = buckets[n]

        while papers < h:
            h -= 1
            papers += buckets[h]
        
        return h