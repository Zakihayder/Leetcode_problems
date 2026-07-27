class Solution(object):
    def maxProduct(self, nums):
        #maximum = max(nums)
        #nums.remove(maximum)
        #return (maximum-1)*(max(nums)-1)
        nums.sort()
        return (nums[len(nums)-1]-1)*(nums[len(nums)-2]-1)
        