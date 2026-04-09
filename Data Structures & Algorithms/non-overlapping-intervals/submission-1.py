class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevend = intervals[0][1]

        for s, e in intervals[1:]:
            if s>=prevend:
                prevend = e
            else:
                res+=1
                prevend = min(prevend, e)
        return res