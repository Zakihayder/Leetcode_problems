class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        count = 1
        nums.sort()
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1]+1 == nums[i]:
                count += 1
            elif nums[i-1] != nums[i]:
                if count > longest:
                    longest = count
                count = 1

        if count > longest:
            longest = count
        return longest
            