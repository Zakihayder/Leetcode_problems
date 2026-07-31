class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums)-1
        else:
    
            left = 0
            k = 1
            for right in range(len(nums)):
                if nums[right] == 0:
                    k -= 1

                if k < 0:
                    if nums[left] == 0:
                        k += 1
                    left += 1

            return len(nums) - left - 1
        