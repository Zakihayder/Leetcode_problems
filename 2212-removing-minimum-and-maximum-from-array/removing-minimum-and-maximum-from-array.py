class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx

        left = max_idx + 1

        right = n - min_idx

        mixed = (min_idx + 1) + (n - max_idx)

        return min(left, right, mixed)

