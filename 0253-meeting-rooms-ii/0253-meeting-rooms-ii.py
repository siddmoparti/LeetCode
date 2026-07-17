class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # start = 0,5,15
        # end = 10,20,30

        start_times = []
        end_times = []
        
        for start,end in intervals:
            start_times.append(start)
            end_times.append(end)
        
        start_times.sort()
        end_times.sort()
        res = 0
        cur = 0
        i = 0
        j = 0
        while i < len(intervals) and j < len(intervals):
            if start_times[i] < end_times[j]:
                cur += 1
                i += 1
            else:
                j += 1
                cur -= 1
            res = max(res, cur)
        return res
            

    


    