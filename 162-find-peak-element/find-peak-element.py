class Solution(object):
    def findPeakElement(self, nums):
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
        if len(nums) >= 2:
            if nums[len(nums)-1] > nums[len(nums)-2]:
                return len(nums)-1
        return 0
        