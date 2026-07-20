class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1,-1]
        else:
            i = nums.index(target)
            nums.reverse()
            return [i,len(nums)-nums.index(target)-1]
        
        
        
        