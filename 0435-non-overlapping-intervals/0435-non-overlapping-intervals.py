class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        removals = 0
        for i in range(1,len(intervals)):
            start = res[-1][0]
            end = res[-1][1]
            if intervals[i][0] < end:
                if end > intervals[i][1]:
                    res.pop()
                    res.append([intervals[i][0], intervals[i][1]])
                removals += 1
                    
            else:
                res.append([intervals[i][0], intervals[i][1]])
        
        return removals
            


            

        