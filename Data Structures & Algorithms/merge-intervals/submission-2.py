class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        print(intervals)
        output = [intervals[0]]
        for start, end in intervals[1:]:
            outputend = output[-1][1]
            if start<=outputend:  # overlapping
                output[-1][1] = max(end, outputend)
            else: # non-overlapping
                output.append([start, end])
        return output
            
