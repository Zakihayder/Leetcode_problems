class Solution(object):
    def singleNumber(self, nums):
        nums.sort()

        for i in range(0,len(nums)-2,3):
            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[len(nums)-1]
            
        