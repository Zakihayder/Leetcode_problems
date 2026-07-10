class Solution(object):
    def merge(self, intervals):

        intervals.sort()

        ans = [intervals[0]]

        for i in range(1, len(intervals)):

            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans