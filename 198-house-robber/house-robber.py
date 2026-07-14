class Solution(object):
    def rob(self, nums):
        
        if len(nums) == 3:
            return max(nums[0]+nums[2],nums[1])
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif len(nums) == 3:
            return nums[0]
        else:
            prev1, prev2 = 0 ,0 

            for num in nums:
                curr = max(prev1, prev2+num)
                prev2, prev1 = prev1, curr
            return curr
            
        
        