class Solution(object):
    def minCostClimbingStairs(self, cost):
        first = second = 0

        for c in cost:
            first, second = second, min(first, second) + c

        return min(first, second)