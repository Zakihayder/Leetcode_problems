class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        removed = 0

        for start, finish in intervals[1:]:
            if start < end:
                removed += 1
            else:
                end = finish

        return removed