class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total = 0
        curr_max, max_sum = 0, float('-inf')
        curr_min, min_sum = 0, float('inf')

        for num in nums:
            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)

            total += num

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)