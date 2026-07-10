class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()

        total = 0
        maximum = 0
        if not nums:
            return 0
            
        for i in range(1,len(nums)):
            if (nums[i-1]+1 == nums[i]):
                total += 1
            elif (nums[i-1] != nums[i]):
                total = 0

            if total > maximum:
                maximum = total
        
        return maximum+1
        