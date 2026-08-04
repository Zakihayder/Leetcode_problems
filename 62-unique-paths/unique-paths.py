from math import comb

class Solution(object):
    def uniquePaths(self, m, n):
        return comb(m + n - 2, m - 1)