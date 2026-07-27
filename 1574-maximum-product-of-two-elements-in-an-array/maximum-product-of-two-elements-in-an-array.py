class Solution(object):
    def maxProduct(self, nums):
        maximum = max(nums)
        nums.remove(maximum)
        return (maximum-1)*(max(nums)-1)
        