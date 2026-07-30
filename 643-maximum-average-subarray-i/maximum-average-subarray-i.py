class Solution(object):
    def findMaxAverage(self, nums, k):
        window = sum(nums[:k])
        best = window

        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            if window > best:
                best = window

        return float(best) / k