class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        if n < 3:
            return n
        else:
             p = 1
        while p <= n:
            p <<= 1

        return p
        