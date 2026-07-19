class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                # ascending at mid -> a peak must exist to the right
                left = mid + 1
            else:
                # descending (or equal-then-descending) at mid -> a peak exists at mid or to the left
                right = mid

        return left  # left == right, pointing at a peak