class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if sum((pile + mid - 1) // mid for pile in piles) <= h:
                right = mid
            else:
                left = mid + 1

        return left