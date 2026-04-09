class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # small so we not need to insert it
            if newInterval[1]< intervals[i][0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            
            # intervals is not overlapping
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            
            else: # overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res